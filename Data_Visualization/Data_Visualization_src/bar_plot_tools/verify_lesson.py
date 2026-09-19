"""執行長條圖 Notebook 程式格、嵌入輸出，並驗證 36 個獨立範例。"""
from pathlib import Path
import base64
import contextlib
import io
import json
import os
import re
import subprocess
import sys
import warnings

os.environ['MPLBACKEND'] = 'Agg'
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK = ROOT / '長條圖_Bar_Plot.ipynb'
DATA = ROOT / 'Data_Visualization_data' / 'bar_plot'
OUT = ROOT / 'Data_Visualization_output' / 'bar_plot'
PREVIEWS = OUT / 'previews'
PREVIEWS.mkdir(parents=True, exist_ok=True)
notebook = json.loads(NOTEBOOK.read_text(encoding='utf-8'))
namespace = {'__name__': '__main__'}
figure_count = 0
outputs = []
stream = io.StringIO()

def flush_text():
    if stream.getvalue():
        outputs.append({'output_type': 'stream', 'name': 'stdout', 'text': stream.getvalue()})
        stream.seek(0)
        stream.truncate(0)

def show(*args, **kwargs):
    global figure_count
    flush_text()
    for number in plt.get_fignums():
        fig = plt.figure(number)
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png', dpi=110, bbox_inches='tight')
        figure_count += 1
        (PREVIEWS / f'{figure_count:02d}.png').write_bytes(buffer.getvalue())
        outputs.append({'output_type': 'display_data', 'metadata': {},
                        'data': {'image/png': base64.b64encode(buffer.getvalue()).decode('ascii'),
                                 'text/plain': [f'<Figure {figure_count}>']}})
    plt.close('all')

plt.show = show
os.chdir(ROOT)
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        compile(cell['source'], f'cell-{i}', 'exec')
    else:
        for link in re.findall(r'\]\(([^)]+)\)', cell['source']):
            if not link.startswith(('https://', 'http://', '#')):
                assert (NOTEBOOK.parent / link).exists(), link

execution_count = 0
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter('always')
    for index, cell in enumerate(notebook['cells']):
        if cell['cell_type'] != 'code':
            continue
        execution_count += 1
        outputs = []
        stream = io.StringIO()
        try:
            with contextlib.redirect_stdout(stream):
                exec(compile(cell['source'], f'cell-{index}', 'exec'), namespace)
                flush_text()
        except Exception:
            print(f'FAILED cell {index}:\n{cell["source"]}')
            raise
        cell['execution_count'] = execution_count
        cell['outputs'] = outputs
    warning_messages = sorted({str(w.message) for w in caught})

NOTEBOOK.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

# 核對教材中的幾個關鍵數值，避免圖能跑但說明與資料不一致。
orders = pd.read_csv(DATA / '03_早餐店訂單明細.csv')
assert len(orders) == 12 and orders['金額'].sum() == 930 and orders['份數'].sum() == 23
budget = pd.read_csv(DATA / '05_預算與實際支出.csv')
assert (budget['實際'] - budget['預算']).sum() == 730
missing = pd.read_csv(DATA / '09_飲料店盤點缺漏.csv')
assert missing['杯數'].isna().sum() == 1 and (missing['杯數'] == 0).sum() == 1
shopping = pd.read_csv(DATA / '12_兩週購物紀錄.csv')
assert shopping['消費金額'].mean() == 80
assert shopping.groupby('週別')['消費金額'].mean().mean() == 125
lunch = pd.read_csv(DATA / '16_練習便當訂購.csv')
assert lunch['份數'].sum() == 53 and (lunch['份數'] * lunch['單價']).sum() == 5445
sales = pd.read_csv(DATA / '13_早餐分店一週銷量.csv')
assert len(sales) == 42 and not sales.duplicated(['日期', '分店', '品項']).any()
assert '\ufffd' not in NOTEBOOK.read_text(encoding='utf-8')

scripts = sorted((ROOT / 'Data_Visualization_src' / 'bar_plot_examples').glob('*.py'))
script_warnings = []
runner = '''
import runpy, sys
import matplotlib.pyplot as plt
def render_show(*args, **kwargs):
    for number in plt.get_fignums():
        plt.figure(number).canvas.draw()
    plt.close('all')
plt.show = render_show
runpy.run_path(sys.argv[1], run_name='__main__')
'''
for script in scripts:
    result = subprocess.run([sys.executable, '-c', runner, str(script)], cwd=ROOT.parent,
                            env={**os.environ, 'PYTHONIOENCODING': 'utf-8'}, capture_output=True)
    if result.returncode:
        print(result.stdout.decode('utf-8', errors='replace'))
        print(result.stderr.decode('utf-8', errors='replace'))
        raise RuntimeError(script.name)
    if result.stderr:
        script_warnings.append((script.name, result.stderr.decode('utf-8', errors='replace')))

thumbnails = []
for preview in sorted(PREVIEWS.glob('*.png')):
    thumb = Image.open(preview).convert('RGB')
    thumb.thumbnail((470, 260))
    canvas = Image.new('RGB', (480, 290), 'white')
    canvas.paste(thumb, ((480 - thumb.width) // 2, 25))
    ImageDraw.Draw(canvas).text((8, 5), preview.stem, fill='black')
    thumbnails.append(canvas)
sheet = Image.new('RGB', (1920, ((len(thumbnails) + 3) // 4) * 290), '#dddddd')
for i, thumb in enumerate(thumbnails):
    sheet.paste(thumb, ((i % 4) * 480, (i // 4) * 290))
sheet.save(PREVIEWS / 'contact_sheet.jpg')
report = {'notebook_code_cells': execution_count, 'figures': figure_count,
          'standalone_examples': len(scripts), 'csv_files': len(list(DATA.glob('*.csv'))),
          'notebook_warnings': warning_messages, 'standalone_stderr': script_warnings,
          'data_checks': 'passed', 'local_links': 'passed',
          'versions': {name: namespace[name].__version__ for name in ['matplotlib', 'sns', 'pd']}}
(OUT / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=True, indent=2))

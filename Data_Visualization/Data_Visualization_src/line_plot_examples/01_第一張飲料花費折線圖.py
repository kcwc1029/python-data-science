# -*- coding: utf-8 -*-
"""範例 01：第一張飲料花費折線圖。詳解請搭配折線圖 Notebook。"""
from pathlib import Path
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import font_manager
import seaborn as sns

# 同時支援從專案根目錄、Notebook 目錄或範例目錄啟動。
start = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
candidates = [start, *start.parents]
ROOT = next((p if (p / "Data_Visualization_data" / "line_plot").is_dir()
             else p / "Data_Visualization"
             for p in candidates
             if (p / "Data_Visualization_data" / "line_plot").is_dir()
             or (p / "Data_Visualization" / "Data_Visualization_data" / "line_plot").is_dir()), None)
if ROOT is None:
    raise FileNotFoundError("請保留 Data_Visualization 整個資料夾，並在專案內執行。")
DATA = ROOT / "Data_Visualization_data" / "line_plot"
OUT = ROOT / "Data_Visualization_output" / "line_plot_lesson"
OUT.mkdir(parents=True, exist_ok=True)

available_fonts = {f.name for f in font_manager.fontManager.ttflist}
font = next((f for f in ["Microsoft JhengHei", "Noto Sans CJK TC", "PingFang TC",
                         "Arial Unicode MS"] if f in available_fonts), "DejaVu Sans")
plt.rcdefaults()
plt.rcParams.update({"font.family": font, "axes.unicode_minus": False,
                     "figure.figsize": (9, 4.5), "font.size": 11})
if font == "DejaVu Sans":
    print("找不到中文字型；請安裝 Noto Sans CJK TC，再重啟 Kernel。")

def read_data(filename, date_col=None):
    """讀取教材 CSV；需要日期運算時才指定日期欄名。"""
    table = pd.read_csv(DATA / filename, encoding="utf-8-sig")
    if date_col is not None:
        table[date_col] = pd.to_datetime(table[date_col], errors="raise")
    return table

def date_axis(ax):
    """把日期刻度放在合理間隔，避免每天的文字擠在一起。"""
    locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))

print("Matplotlib", matplotlib.__version__, "Seaborn", sns.__version__, "Pandas", pd.__version__)
print("資料位置：", DATA)

星期 = ["一", "二", "三", "四", "五", "六", "日"]
飲料費 = [35, 65, 0, 70, 55, 90, 40]
fig, ax = plt.subplots()
ax.plot(星期, 飲料費, marker="o")
ax.set(title="這週飲料費花在哪一天？", xlabel="星期", ylabel="飲料費（元）")
ax.set_ylim(bottom=0)
plt.show()
print("本週合計：", sum(飲料費), "元")

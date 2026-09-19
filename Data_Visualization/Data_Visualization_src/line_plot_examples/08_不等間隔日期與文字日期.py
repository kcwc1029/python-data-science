# -*- coding: utf-8 -*-
"""範例 08：不等間隔日期與文字日期。詳解請搭配折線圖 Notebook。"""
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

df = pd.DataFrame({"日期": ["2026-04-01", "2026-04-02", "2026-04-10"], "飲料費": [40, 60, 50]})
fig, axes = plt.subplots(1, 2, figsize=(12, 4), sharey=True, layout="constrained")
axes[0].plot(df["日期"], df["飲料費"], marker="o")
axes[0].set_title("文字標籤：三次紀錄等距排列")
axes[1].plot(pd.to_datetime(df["日期"]), df["飲料費"], marker="o")
axes[1].set_title("日期座標：保留相隔天數")
date_axis(axes[1])
for ax in axes:
    ax.set(xlabel="日期", ylabel="飲料費（元）")
plt.show()

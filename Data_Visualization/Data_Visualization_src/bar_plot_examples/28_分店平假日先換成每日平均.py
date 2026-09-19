# -*- coding: utf-8 -*-
"""範例 28：分店平假日先換成每日平均。完整講解見長條圖 Notebook。"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.container import BarContainer
import seaborn as sns

# 從 Notebook、專案根目錄或獨立範例檔啟動，都能找到教材資料。
start = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
ROOT = next((candidate for parent in [start, *start.parents]
             for candidate in [parent, parent / "Data_Visualization"]
             if (candidate / "Data_Visualization_data" / "bar_plot").is_dir()), None)
if ROOT is None:
    raise FileNotFoundError("找不到 bar_plot 資料，請保留整個 Data_Visualization 資料夾並在專案內啟動。")
DATA = ROOT / "Data_Visualization_data" / "bar_plot"
OUT = ROOT / "Data_Visualization_output" / "bar_plot"
OUT.mkdir(parents=True, exist_ok=True)

font_names = {f.name for f in font_manager.fontManager.ttflist}
font = next((name for name in ["Microsoft JhengHei", "Noto Sans CJK TC", "PingFang TC",
                              "Arial Unicode MS"] if name in font_names), "DejaVu Sans")
plt.rcdefaults()
plt.rcParams.update({"font.family": font, "axes.unicode_minus": False,
                     "figure.figsize": (9, 5), "font.size": 11})
if font == "DejaVu Sans":
    print("未找到中文字型；請安裝 Noto Sans CJK TC，重啟 Kernel 後重跑設定。")

def read_data(filename):
    return pd.read_csv(DATA / filename, encoding="utf-8-sig")

def label_bars(ax, fmt="%.0f", padding=3):
    # Seaborn 的群組圖可能回傳多組長條；只對長條容器加標籤。
    for container in ax.containers:
        if isinstance(container, BarContainer):
            ax.bar_label(container, fmt=fmt, padding=padding)

print("Matplotlib", matplotlib.__version__, "Seaborn", sns.__version__, "Pandas", pd.__version__)
print("資料位置：", DATA)

df = read_data("13_早餐分店一週銷量.csv")
daily = df.groupby(["日期", "日別", "分店"], as_index=False)["份數"].sum()
summary = daily.groupby(["分店", "日別"], as_index=False).agg(每日平均=("份數", "mean"), 營業天數=("日期", "nunique"))
print(summary)
g = sns.catplot(data=summary, x="日別", y="每日平均", col="分店", kind="bar",
                order=["平日", "假日"], estimator="mean", errorbar=None, color="#0072B2",
                height=4, aspect=0.9, sharey=True)
g.set_axis_labels("日別", "每日平均總份數（份／日）")
g.set_titles("{col_name}")
for ax in g.axes.flat:
    label_bars(ax, fmt="%.1f")
    ax.set_ylim(0, summary["每日平均"].max() * 1.2)
g.figure.suptitle("同一週：五個平日、兩個假日；三店每天均營業", y=1.05)
g.savefig(OUT / "28_分店每日平均.png", dpi=160)
plt.show()

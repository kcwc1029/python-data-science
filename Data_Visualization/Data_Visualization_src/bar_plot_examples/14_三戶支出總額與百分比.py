# -*- coding: utf-8 -*-
"""範例 14：三戶支出總額與百分比。完整講解見長條圖 Notebook。"""
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

df = read_data("08_三戶租屋支出.csv")
parts = ["房租", "餐費", "交通", "其他"]
amounts = df[parts]
totals = amounts.sum(axis=1)
assert (totals > 0).all()
percent = amounts.div(totals, axis=0) * 100
fig, axes = plt.subplots(1, 2, figsize=(13, 5), layout="constrained")
for ax, table, title, unit in zip(axes, [amounts, percent], ["每月總額與組成", "每戶自己的支出占比"], ["元／月", "%"]):
    bottom = np.zeros(len(df))
    for part in parts:
        bars = ax.bar(df["住戶"], table[part], bottom=bottom, label=part)
        if unit == "%":
            ax.bar_label(bars, fmt="%.1f%%", label_type="center", fontsize=9)
        bottom += table[part].to_numpy()
    ax.set(title=title, xlabel="住戶", ylabel=unit)
axes[0].set_ylim(0, totals.max() * 1.25)
axes[0].legend(ncols=2, fontsize=9)
axes[1].set_ylim(0, 100)
plt.show()
print(pd.DataFrame({"住戶": df["住戶"], "總支出": totals}))

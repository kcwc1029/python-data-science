# -*- coding: utf-8 -*-
"""範例 26：平均中位數與原始等待點。完整講解見長條圖 Notebook。"""
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

df = read_data("11_早餐店等候紀錄.csv")
order = ["巷口早餐店", "車站早餐店", "市場早餐店"]
fig, axes = plt.subplots(1, 2, figsize=(13, 5), sharey=True, layout="constrained")
for ax, estimator, title in zip(axes, ["mean", "median"], ["平均與所有觀測", "中位數與所有觀測"]):
    sns.barplot(data=df, x="店家", y="等候分鐘", order=order, estimator=estimator,
                errorbar=None, color="#B9DDEB", ax=ax)
    sns.stripplot(data=df, x="店家", y="等候分鐘", order=order, jitter=False,
                  color="#333333", size=5, alpha=0.6, ax=ax)
    label_bars(ax, fmt="%.1f")
    ax.set(title=title, xlabel="店家", ylabel="等候（分鐘）")
plt.show()
print(df.groupby("店家")["等候分鐘"].agg(["mean", "median", "max"]))

# -*- coding: utf-8 -*-
"""範例 18：超市比價報告與輸出。完整講解見長條圖 Notebook。"""
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

df = read_data("10_超市雞蛋包裝比價.csv")
df["每顆單價"] = df["盒價"] / df["顆數"]
df = df.sort_values("每顆單價")
fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
bars = ax.barh(df["商品"], df["每顆單價"], color="#0072B2")
ax.invert_yaxis()
ax.bar_label(bars, fmt="%.2f", padding=4)
ax.set(title="同等級雞蛋包裝比價｜虛構教學價格", xlabel="元／顆", ylabel="商品", xlim=(0, 10))
fig.savefig(OUT / "18_雞蛋單價比較.png", dpi=160, bbox_inches="tight")
fig.savefig(OUT / "18_雞蛋單價比較.svg", bbox_inches="tight")
df.to_csv(OUT / "18_雞蛋單價摘要.csv", index=False, encoding="utf-8-sig")
plt.show()
print(f"在本題同等級的假設下，最低每顆單價為 {df.iloc[0]['每顆單價']:.2f} 元。")
print("尚未納入保存期限、促銷與吃不完的浪費。")

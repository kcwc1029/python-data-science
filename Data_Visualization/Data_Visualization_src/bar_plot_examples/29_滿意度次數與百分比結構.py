# -*- coding: utf-8 -*-
"""範例 29：滿意度次數與百分比結構。完整講解見長條圖 Notebook。"""
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

df = read_data("14_便當店滿意度次數.csv")
levels = ["非常不滿意", "不滿意", "普通", "滿意", "非常滿意"]
totals = df[levels].sum(axis=1)
percent = df[levels].div(totals, axis=0) * 100
colors = sns.color_palette("RdYlBu", n_colors=5)
fig, ax = plt.subplots(figsize=(11, 5), layout="constrained")
left = np.zeros(len(df))
for level, color in zip(levels, colors):
    values = percent[level].to_numpy()
    bars = ax.barh(df["店家"], values, left=left, label=level, color=color)
    ax.bar_label(bars, labels=[f"{v:.1f}%" if v >= 9 else "" for v in values], label_type="center", fontsize=9)
    left += values
ax.set_yticks(np.arange(len(df)), [f"{shop}（n={n}）" for shop, n in zip(df["店家"], totals)])
ax.invert_yaxis()
ax.set(title="各店受訪者滿意度結構（虛構便利取樣）", xlabel="占各店有效回覆（%）", ylabel="店家", xlim=(0, 100))
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncols=5, fontsize=9)
plt.show()
print(percent.round(1))

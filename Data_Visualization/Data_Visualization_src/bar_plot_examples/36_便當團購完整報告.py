# -*- coding: utf-8 -*-
"""範例 36：便當團購完整報告。完整講解見長條圖 Notebook。"""
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

df = read_data("16_練習便當訂購.csv")
assert not df.duplicated(["班別", "口味"]).any()
assert (df["份數"] >= 0).all() and (df["單價"] > 0).all()
df["金額"] = df["份數"] * df["單價"]
summary = df.groupby("班別", as_index=False).agg(總份數=("份數", "sum"), 應收金額=("金額", "sum"))
summary["每份平均金額"] = summary["應收金額"] / summary["總份數"]
assert summary["總份數"].sum() == df["份數"].sum()
fig, axes = plt.subplots(1, 2, figsize=(13, 5), layout="constrained")
sns.barplot(data=df, x="口味", y="份數", hue="班別", order=["雞腿", "排骨", "蔬食"],
            hue_order=["早班", "晚班"], palette={"早班": "#0072B2", "晚班": "#D55E00"},
            estimator="sum", errorbar=None, gap=0.1, ax=axes[0])
sns.barplot(data=summary, x="班別", y="應收金額", order=["早班", "晚班"], estimator="sum",
            errorbar=None, color="#009E73", ax=axes[1])
axes[0].set(title="每班每口味訂購份數", xlabel="口味", ylabel="份數（份）", ylim=(0, 17))
axes[1].set(title="依份數與單價計算的應收金額", xlabel="班別", ylabel="金額（元）", ylim=(0, 3500))
for ax in axes:
    label_bars(ax)
fig.suptitle("同日便當團購核對｜虛構資料；未含另計運費與折扣")
fig.savefig(OUT / "36_便當團購報告.png", dpi=160, bbox_inches="tight")
fig.savefig(OUT / "36_便當團購報告.svg", bbox_inches="tight")
summary.to_csv(OUT / "36_各班應收摘要.csv", index=False, encoding="utf-8-sig")
df.to_csv(OUT / "36_便當訂購核對明細.csv", index=False, encoding="utf-8-sig")
plt.show()
print(summary.round(2))
print("共訂", df["份數"].sum(), "份；應收", df["金額"].sum(), "元。")

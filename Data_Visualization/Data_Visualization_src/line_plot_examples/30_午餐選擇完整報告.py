# -*- coding: utf-8 -*-
"""範例 30：午餐選擇完整報告。詳解請搭配折線圖 Notebook。"""
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

df = read_data("11_午餐取得方式.csv", "日期").sort_values("日期")
methods = ["自備便當", "店內購買", "外送到家"]
long = df.melt(id_vars="日期", value_vars=methods, var_name="方式", value_name="費用")
long = long.sort_values(["方式", "日期"])
long["累積費用"] = long.groupby("方式")["費用"].cumsum()
summary = long.groupby("方式")["費用"].agg(["count", "sum", "mean", "max"]).reindex(methods)
summary.columns = ["觀測餐數", "總費用", "平均每餐", "最高單餐"]
colors = {"自備便當": "#009E73", "店內購買": "#0072B2", "外送到家": "#D55E00"}
fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True, layout="constrained")
for ax, column, title in zip(axes, ["費用", "累積費用"], ["每天花多少", "十天累積到多少"]):
    sns.lineplot(data=long, x="日期", y=column, hue="方式", style="方式", palette=colors,
                 hue_order=methods, markers=True, estimator=None, errorbar=None, ax=ax)
    ax.set(title=title, xlabel="日期", ylabel=f"{column}（元）")
    date_axis(ax)
fig.suptitle("午餐費用情境比較｜自備未計工時，外送含附加費")
fig.savefig(OUT / "30_午餐選擇報告.png", dpi=160, bbox_inches="tight")
summary.to_csv(OUT / "30_午餐費用摘要.csv", encoding="utf-8-sig")
plt.show()
print(summary.round(1))
gap = summary.loc["外送到家", "總費用"] - summary.loc["自備便當", "總費用"]
print(f"這十餐的外送與自備材料費差額為 {gap:.0f} 元。")
print("限制：這是虛構情境，自備未計工時，不能直接推估所有人的全年支出。")

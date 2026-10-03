- [基本Matplotlib設定](./基本Matplotlib設定.ipynb)
- [基本Seaborn設定](./基本Seaborn設定.ipynb)
- [折線圖 Line Plot](./Line_Plot/折線圖.ipynb)
- [長條圖 Bar Plot](./bar_plot/長條圖.ipynb)
- [散佈圖 Scatter Plot](./Scatter_Plot/散佈圖.ipynb)
- [直方圖 Histogram](./Histogram/直方圖.ipynb)
- [圓餅圖 Pie_Chart](./Pie_Chart/圓餅圖.ipynb)
- [箱型圖 Box_Plot](./Box_Plot/箱型圖.ipynb)
- [熱圖 Heatmap](./Heatmap/熱圖.ipynb)

### 很常用到視覺化作圖開頭

```python
import pandas as pd

df = pd.read_csv("./datasets/通勤時間.csv", encoding="utf-8-sig")
df
```

```python
import matplotlib.pyplot as plt

with plt.style.context("default"):
	# 中文設定
	plt.rcParams["font.family"] = "Microsoft JhengHei" # Windows 微軟正黑體
	plt.rcParams["axes.unicode_minus"] = False # 避免負號顯示異常
	fig, ax = plt.subplots(figsize=(6, 4))
```

```python
import matplotlib.pyplot as plt
import seaborn as sns

with sns.axes_style("whitegrid"): # 套用 Seaborn 樣式
	# 中文設定
	plt.rcParams["font.family"] = "Microsoft JhengHei" # Windows 微軟正黑體
	plt.rcParams["axes.unicode_minus"] = False # 避免負號顯示異常
	fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True, layout="constrained")
```

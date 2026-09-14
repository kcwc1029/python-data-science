"""NumPy 與 Pandas：標籤和位置的交接。對應 numpy.md 第 19 節。"""

from pathlib import Path
import numpy as np
import pandas as pd

# 從程式本身的位置找章節資料夾，避免受終端機所在目錄影響。
BASE = Path(__file__).resolve().parents[1]
output_dir = BASE / "numpy_outputs"
output_dir.mkdir(parents=True, exist_ok=True)
orders = pd.read_csv(BASE / "numpy_datasets" / "lunch_orders.csv")
# 欄位順序固定為單價、份數，並使用獨立浮點數陣列。
values = orders[["單價", "份數"]].to_numpy(dtype=float, copy=True)
subtotals = values[:, 0] * values[:, 1]
report = orders.copy()
report["小計"] = subtotals
report.to_csv(output_dir / "lunch_report.csv", index=False, encoding="utf-8-sig")
print(report)
print("整筆訂單：", np.sum(subtotals))
# 示範標籤對齊與位置對齊的差異。
a = pd.Series([100, 200], index=["小安", "小美"])
b = pd.Series([20, 10], index=["小美", "小安"])
print("Pandas 按姓名：\n", a + b)
print("NumPy 按位置：", a.to_numpy() + b.to_numpy())

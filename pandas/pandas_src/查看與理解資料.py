"""建立拿到陌生資料後的固定健康檢查流程。"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
path = BASE_DIR / "Pandas_datasets" / "個人消費紀錄_髒資料.csv"
df = pd.read_csv(path)

df.info()
# print("前 5 列：\n", df.head())
# print("\n後 3 列：\n", df.tail(3))
# print("\n列數、欄數：", df.shape)
# print("\n欄名：", df.columns.tolist())
# print("\n資料型態與非空值：")
# print("\n包含文字欄位的摘要：\n", df.describe(include="all"))
# print("\n每欄缺失值數量：\n", df.isna().sum())

import pandas as pd

### 建立 DataFrame
data = {
    "姓名": ["小明", "小美", "小華", "小安"],
    "商品": ["珍珠奶茶", "雞排", "咖啡", "便當"],
    "金額": [65, 80, 55, 120]
}

df = pd.DataFrame(data)

### 匯出 CSV
df.to_csv(
    "orders.csv",
    index=False,
    encoding="utf-8-sig"
) # 將 DataFrame 儲存成 CSV，不輸出索引欄位

print("\n已建立 orders.csv")

### 讀取 CSV
orders_df = pd.read_csv(
    "orders.csv",
    encoding="utf-8-sig"
) # 將剛才建立的 CSV 重新讀取成 DataFrame


### 顯示讀取結果
print("\n從 CSV 讀取的資料：")
print(orders_df)
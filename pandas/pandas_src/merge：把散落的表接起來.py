import pandas as pd


### 建立訂單資料
orders_data = {
    "訂單編號": ["A001", "A002", "A003", "A004"],
    "店家編號": ["S01", "S02", "S01", "S03"],
    "金額": [180, 320, 250, 450]
}

orders = pd.DataFrame(orders_data)

### 建立店家資料
shops_data = {
    "店家編號": ["S01", "S02", "S03"],
    "店家名稱": ["阿明便當", "珍珠奶茶店", "老王牛肉麵"],
    "類別": ["便當", "飲料", "麵食"]
}

shops = pd.DataFrame(shops_data)


# 現在兩張表都有「店家編號」，所以可以使用它當作合併依據。
### 使用店家編號合併兩張資料表
result = orders.merge(
    shops,
    on="店家編號"
)

print(result)

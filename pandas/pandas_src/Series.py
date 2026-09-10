import pandas as pd


### 建立 Series
lunch_cost = pd.Series(
    data=[95, 120, 80, 150, 110],
    index=["星期一", "星期二", "星期三", "星期四", "星期五"],
    name="午餐費",
    dtype="int64"
)


### 顯示完整 Series
print("午餐費：")
print(lunch_cost)


### 查看 Series 的基本資訊
print("\nvalues：")
print(lunch_cost.values)

print("\nindex：")
print(lunch_cost.index)

print("\ndtype：")
print(lunch_cost.dtype)

print("\nname：")
print(lunch_cost.name)
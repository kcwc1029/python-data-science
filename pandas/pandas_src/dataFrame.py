import pandas as pd

### 建立 DataFrame
data = {
    "姓名": ["小明", "小美", "小華", "小傑"],
    "國文": [85, 92, 78, 88],
    "英文": [90, 95, 72, 84],
    "數學": [88, 89, 95, 76]
}

df = pd.DataFrame(
    data,
    index=["S001", "S002", "S003", "S004"]
)


### 顯示 DataFrame
print("學生成績表：")
print(df)

### 查看基本資訊
print("\nindex：")
print(df.index)

print("\ncolumns：")
print(df.columns)

print("\nvalues：")
print(df.values)

print("\ndtypes：")
print(df.dtypes)

print("\nshape：")
print(df.shape)
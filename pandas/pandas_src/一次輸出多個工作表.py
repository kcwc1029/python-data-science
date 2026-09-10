import pandas as pd

### 建立全班成績資料
scores = pd.DataFrame({
    "姓名": ["小明", "小美", "小華", "小傑", "小芳"],
    "國文": [85, 92, 55, 78, 48],
    "英文": [90, 88, 50, 82, 55],
    "數學": [88, 95, 45, 70, 52]
})

### 計算平均成績
scores["平均"] = scores[["國文", "英文", "數學"]].mean(axis=1)

### 找出平均不及格的學生
failed = scores[scores["平均"] < 60]

### 顯示資料
print("全班成績：")
print(scores)

print("\n不及格名單：")
print(failed)

### 寫入同一個 Excel 的不同工作表
with pd.ExcelWriter("../pandas_output/學生成績報表.xlsx", engine="openpyxl") as writer:
    scores.to_excel(writer, sheet_name="全班成績", index=False)
    failed.to_excel(writer, sheet_name="不及格名單", index=False)


### 執行完成
print("\nExcel 匯出完成")
print("已產生：學生成績報表.xlsx")
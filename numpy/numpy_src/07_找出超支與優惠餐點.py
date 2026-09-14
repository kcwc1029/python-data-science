"""布林遮罩：把消費條件變成篩選器。對應 numpy.md 第 07 節。"""

import numpy as np

names = np.array(["雞腿飯", "湯麵", "咖哩飯", "水餃", "排骨飯"])
prices = np.array([130, 75, 110, 80, 120])
# 兩個條件分別加括號，再逐格取交集。
mask = (prices >= 80) & (prices <= 120)
print("遮罩：", mask)
print("可選餐點：", names[mask])
print("對應價格：", prices[mask])
print("符合數量：", mask.sum())
print("是否有超過 125 元：", (prices > 125).any())
# 直接對原陣列的選定位置更新。
prices[prices > 120] -= 10
print("優惠後：", prices)

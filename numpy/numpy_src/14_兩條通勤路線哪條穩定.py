"""統計與聚合：平均以外還要看什麼。對應 numpy.md 第 14 節。"""

import numpy as np

route_a = np.array([28, 30, 32, 30, 30])
route_b = np.array([10, 20, 30, 40, 50])
for name, route in [("A 路線", route_a), ("B 路線", route_b)]:
    print(name, "總時間", route.sum(), "平均", route.mean())
    print("最短", route.min(), "最長", route.max(), "標準差", route.std())
# 手動拆開標準差計算，與 NumPy 比較。
values = np.array([20, 30, 40])
deviations = values - values.mean()
manual_std = np.sqrt((deviations ** 2).mean())
print("手算標準差：", manual_std)
print("NumPy 標準差：", values.std())
print("被大額拉高的平均：", np.mean([80, 90, 100, 110, 1000]))
print("中位數：", np.median([80, 90, 100, 110, 1000]))

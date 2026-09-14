"""排序與唯一值：保留姓名與數字的配對。對應 numpy.md 第 17 節。"""

import numpy as np

shops = np.array(["巷口", "車站", "市場", "公司旁"])
prices = np.array([110, 95, 95, 120])
# stable 讓同價商品保留原先的先後順序。
order = np.argsort(prices, kind="stable")
print("排序位置：", order)
print("店名：", shops[order])
print("價格：", prices[order])
values, counts = np.unique(prices, return_counts=True)
print("價格種類：", values, "各有幾家：", counts)
# 小班級示範競賽排名；大型資料可改用更節省空間的方法。
scores = np.array([90, 90, 80])
ranks = 1 + (scores[None, :] > scores[:, None]).sum(axis=1)
print("同分同名次：", ranks)

"""廣播機制：不同形狀如何配對。對應 numpy.md 第 12 節。"""

import numpy as np

# 三戶家庭，兩欄分別是牛奶與雞蛋的購買數量。
quantities = np.array([[2, 1], [1, 3], [4, 2]])
prices = np.array([80, 60])
subtotals = quantities * prices  # (3,2) 配 (2,)。
# 每戶各自有一個折扣，要沿該戶的兩種商品套用。
discounts = np.array([0.9, 1.0, 0.8]).reshape(-1, 1)
discounted = subtotals * discounts
print("原小計：\n", subtotals)
print("折扣後小計：\n", discounted)
print("每戶應付：", discounted.sum(axis=1))

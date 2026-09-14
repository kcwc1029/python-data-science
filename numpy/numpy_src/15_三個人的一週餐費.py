"""理解 axis：被彙整掉的是哪一軸。對應 numpy.md 第 15 節。"""

import numpy as np

# 三個人、四天餐費。
costs = np.array([[80, 100, 120, 100], [90, 90, 90, 90], [100, 110, 120, 130]])
print("每天全體總額：", costs.sum(axis=0))
print("每人四天總額：", costs.sum(axis=1))
print("全部總額：", costs.sum())
personal_mean = costs.mean(axis=1, keepdims=True)
print("個人平均形狀：", personal_mean.shape)
print("各天與自己的平均差：\n", costs - personal_mean)

"""調整形狀：重新排版，不是重新排序。對應 numpy.md 第 09 節。"""

import numpy as np

# 十四天依日期先後存放的餐費。
costs = np.arange(80, 220, 10)
weeks = costs.reshape(2, 7)
print("兩週：\n", weeks)
print("推算欄數：", costs.reshape(2, -1).shape)
print("同星期跨週比較：\n", weeks.T)
print("攤平：", weeks.ravel())
print("一維轉置：", costs.T.shape)
print("真正直欄：", costs.reshape(-1, 1).shape)
# 若要一份可以任意修改的排版結果，明確複製。
independent = weeks.T.copy()
independent[0, 0] = 0
print("原餐費仍是：", costs[0])

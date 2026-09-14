"""向量化：把共同規則寫一次。對應 numpy.md 第 11 節。"""

import numpy as np

prices = np.array([90, 110, 80])
quantities = np.array([2, 1, 3])
# 先用熟悉的方式算，作為對照。
loop_total = 0
for price, quantity in zip(prices, quantities):
    loop_total += price * quantity
# 向量化保留每項小計，方便對帳。
subtotals = prices * quantities
print("各項小計：", subtotals)
print("迴圈總額：", loop_total)
print("陣列總額：", subtotals.sum())
# 本例假設每份收 5 元包裝費，並非每種商品只收一次。
print("含包裝費：", ((prices + 5) * quantities).sum())

"""數學函式與條件運算。對應 numpy.md 第 13 節。"""

import numpy as np

orders = np.array([320, 500, 780])
shipping = np.where(orders >= 500, 0, 60)
print("運費：", shipping)
print("應付：", orders + shipping)
print("點數限制：", np.clip(np.array([-5, 30, 150]), 0, 100))
print("箱數：", np.ceil(np.array([6, 7, 12]) / 6).astype(int))
print("和目標差距：", np.abs(orders - 500))
print("平方根：", np.sqrt(np.array([4, 9, 16])))
# 分母為零的會員暫無訂單，平均消費保留為 0。
count = np.array([2, 0, 3])
total = np.array([300, 0, 900])
average = np.divide(total, count, out=np.zeros(3), where=count != 0)
print("平均消費：", average)

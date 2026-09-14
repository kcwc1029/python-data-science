"""索引與切片：取出想看的時間區間。對應 numpy.md 第 06 節。"""

import numpy as np

# 列為週一到週五，欄為去程與回程，單位分鐘。
commute = np.array([[30, 35], [28, 40], [32, 33], [45, 50], [29, 31]])
print("週三回程：", commute[2, 1])
print("最後一天：", commute[-1])
print("前三天：\n", commute[:3])
print("所有去程：", commute[:, 0])
print("去程保留二維：", commute[:, 0:1].shape)
print("隔天觀察：\n", commute[::2])

"""陣列合併與拆分。對應 numpy.md 第 10 節。"""

import numpy as np

morning = np.array([[10, 20, 30], [15, 25, 35]])
evening = np.array([[8, 12, 16], [9, 13, 17]])
print("沿列接：", np.concatenate([morning, evening], axis=0).shape)
print("沿欄接：", np.concatenate([morning, evening], axis=1).shape)
# 新增班別軸，保留兩張表的身分。
by_shift = np.stack([morning, evening], axis=0)
print("班別、日期、商品：", by_shift.shape)
# 十個號碼分給三組，不必每組一樣多。
for number, group in enumerate(np.array_split(np.arange(1, 11), 3), start=1):
    print(f"第 {number} 組：", group)

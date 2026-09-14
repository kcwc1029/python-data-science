"""資料型態與轉換：數字外觀不等於數字。對應 numpy.md 第 05 節。"""

import numpy as np

# 字串中的純數字可轉為浮點數；「待確認」則不能直接 astype。
price_text = np.array(["120", "85.5", "99.9"])
prices = price_text.astype(float)
print("九折：", prices * 0.9)
print("截去小數：", np.array([3.8, -3.8]).astype(int))
# 先轉浮點數，才能保留修改後的小數。
editable = np.array([100, 200]).astype(float)
editable[0] = 89.5
print("修改後：", editable)
print("浮點比較：", np.isclose(0.1 + 0.2, 0.3))
print("取最近偶數：", np.round([2.5, 3.5]))

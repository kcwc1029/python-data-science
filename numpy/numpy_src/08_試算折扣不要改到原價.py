"""修改陣列：view 與 copy。對應 numpy.md 第 08 節。"""

import numpy as np

original = np.array([100, 120, 150, 180])
alias = original  # 同一個陣列的另一個名字。
view = original[:2]  # 新的觀察窗口，資料仍共用。
trial = original[:2].copy()  # 獨立試算資料。
view[0] = 90
trial[1] = 1
print("原始資料也被 view 改了：", original)
print("獨立試算：", trial)
print("alias 是同物件：", alias is original)
print("view 共用資料：", np.shares_memory(original, view))
print("trial 共用資料：", np.shares_memory(original, trial))
# 進階索引取得複本，修改取出的結果不會回寫。
selected = original[[0, 2]]
selected[0] = 0
print("修改 selected 後的原始資料：", original)

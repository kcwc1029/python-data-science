"""隨機資料：可重現的抽籤與模擬。對應 numpy.md 第 18 節。"""

import numpy as np

rng = np.random.default_rng(42)
people = np.array(["小安", "小美", "阿哲", "怡君", "志明"])
print("兩位分享者：", rng.choice(people, size=2, replace=False))
print("分享順序：", rng.permutation(people))
print("模擬七天客數：", rng.integers(20, 51, size=7))
# 兩個全新產生器使用相同種子與相同第一個呼叫。
a = np.random.default_rng(7).integers(1, 7, size=10)
b = np.random.default_rng(7).integers(1, 7, size=10)
print("兩份結果一致：", np.array_equal(a, b))
# 同一個產生器繼續往下抽，不重設種子。
print("下一週客數：", rng.integers(20, 51, size=7))

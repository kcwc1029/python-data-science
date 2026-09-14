"""跨節練習二：家庭團購，運費依折扣後總額判斷。"""
import numpy as np

prices = np.array([80, 60, 50])
quantities = np.array([[2, 1, 1], [4, 2, 2], [1, 1, 3]])
discounts = np.array([0.9, 1.0, 0.8])
subtotals = quantities * prices  # 單價按商品欄配對。
discounted = subtotals * discounts[:, None]  # 折扣按家庭列配對。
totals = discounted.sum(axis=1)
shipping = np.where(totals >= 500, 0, 60)
print("原商品總額：", subtotals.sum(axis=1))
print("折扣後：", totals)
print("運費：", shipping)
print("應付：", totals + shipping)
print("全部共：", (totals + shipping).sum())
# 以下能執行，卻錯把每戶折扣當成每種商品折扣。
print("錯誤套用的各格：\n", subtotals * discounts)

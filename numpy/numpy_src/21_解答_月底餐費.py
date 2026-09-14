"""跨節練習一：月底餐費。"""
import numpy as np

# 每列一天，每欄依序是早餐、午餐、晚餐。
costs = np.array([[50, 100, 120], [60, 90, 100], [40, 120, 150],
                  [55, 110, 100], [50, 80, 90]])
print("shape、ndim、size：", costs.shape, costs.ndim, costs.size)
daily = costs.sum(axis=1)  # 彙整餐別，留下每天。
print("每天總額：", daily)
print("各餐別總額：", costs.sum(axis=0))
print("超支日期：", np.arange(1, len(costs) + 1)[daily > 250])
trial = costs.copy()  # 修改試算時保留原始餐費。
trial[:, 1] -= 20
print("原總額：", costs.sum())
print("新總額：", trial.sum())
print("省下：", costs.sum() - trial.sum())
print("原午餐仍是：", costs[:, 1])

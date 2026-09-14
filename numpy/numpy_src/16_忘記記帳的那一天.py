"""缺失值：沒有記錄不等於零。對應 numpy.md 第 16 節。"""

import numpy as np

costs = np.array([100, np.nan, 120, 0], dtype=float)
print("缺失位置：", np.isnan(costs))
print("一般平均：", costs.mean())
print("已知資料平均：", np.nanmean(costs))
print("有效筆數：", (~np.isnan(costs)).sum())
# 只做情境試算，保留原始資料，避免混淆補值與實際記錄。
filled = np.where(np.isnan(costs), np.nanmean(costs), costs)
print("平均補值的試算：", filled)
# 第二欄全部沒有記錄，保留 NaN，不冒稱平均為零。
table = np.array([[100, np.nan], [120, np.nan]])
counts = (~np.isnan(table)).sum(axis=0)
means = np.divide(np.nansum(table, axis=0), counts,
                  out=np.full(table.shape[1], np.nan), where=counts > 0)
print("各欄有效筆數：", counts)
print("各欄平均：", means)

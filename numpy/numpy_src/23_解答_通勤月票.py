"""跨節練習三：以不同缺失假設比較虛構月票情境。"""
from pathlib import Path
import numpy as np
import pandas as pd

fares = np.array([60, 60, 80, np.nan, 60, 0, 80, 60, 60, 80])
valid = ~np.isnan(fares)
print("有效天數：", valid.sum(), "缺失天數：", (~valid).sum())
print("已知總額：", np.nansum(fares))
print("已知日平均、中位數、標準差：", np.nanmean(fares),
      np.nanmedian(fares), np.nanstd(fares))
print("僅依有效日推估：", np.nanmean(fares) * 20)
rows = []
for assumed in [0, 60, 120]:
    # 每次由原始資料建立情境，避免前次補值影響下一次。
    scenario = np.where(valid, fares, assumed)
    monthly = scenario.mean() * 20
    rows.append({"情境": f"漏記日假設 {assumed} 元", "補值假設": assumed,
                 "估計月支出": monthly, "估計支出減月票價": monthly - 1200})
report = pd.DataFrame(rows)
output = Path(__file__).resolve().parents[1] / "numpy_outputs"
output.mkdir(parents=True, exist_ok=True)
report.to_csv(output / "commute_scenarios.csv", index=False, encoding="utf-8-sig")
print(report.to_string(index=False))

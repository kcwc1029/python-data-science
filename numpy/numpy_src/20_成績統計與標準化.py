"""完整實作：成績統計、排名與標準化。對應 numpy.md 第 20 節。"""

from pathlib import Path
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
OUTPUT = BASE / "numpy_outputs"
SUBJECTS = ["餐飲實作", "服務溝通", "安全衛生"]
WEIGHTS = np.array([0.5, 0.3, 0.2])


def analyze(input_path, output_dir):
    """依本教材規則分析成績，所有產物寫入指定輸出資料夾。"""
    raw = pd.read_csv(input_path, dtype=str, keep_default_na=False)
    required = ["學號", "姓名", *SUBJECTS]
    if not set(required).issubset(raw.columns):
        raise ValueError("CSV 缺少學號、姓名或指定科目欄位")
    if raw.empty:
        raise ValueError("成績表沒有學生，請先補入資料")
    raw["學號"] = raw["學號"].str.strip()
    raw["姓名"] = raw["姓名"].str.strip()
    if raw["學號"].eq("").any() or raw["學號"].duplicated().any():
        raise ValueError("學號不可空白或重複，請回查原始紀錄")
    if raw["姓名"].eq("").any():
        raise ValueError("姓名不可空白，請回查原始紀錄")
    if WEIGHTS.shape != (len(SUBJECTS),) or not np.isclose(WEIGHTS.sum(), 1):
        raise ValueError("每科需有一個權重，且權重總和須為 1")
    if (WEIGHTS < 0).any():
        raise ValueError("權重不可為負數")

    # 字串先保留，品質報告才能呈現原本填了什麼。
    numeric = raw[SUBJECTS].apply(pd.to_numeric, errors="coerce")
    scores = numeric.to_numpy(dtype=float, copy=True)
    valid = np.isfinite(scores) & (scores >= 0) & (scores <= 100)
    issues = []
    for row, col in zip(*np.where(~valid)):
        original = raw.iloc[row][SUBJECTS[col]]
        if original.strip() == "":
            reason = "缺失"
        elif np.isnan(scores[row, col]):
            reason = "非數字或 NaN 文字"
        else:
            reason = "非有限數值或超出 0 到 100"
        issues.append({"學號": raw.iloc[row]["學號"], "科目": SUBJECTS[col],
                       "原始值": original, "問題": reason})
    scores[~valid] = np.nan

    # 先算筆數，再安全除法，讓全缺失欄保留 NaN。
    counts = valid.sum(axis=0)
    means = np.divide(np.nansum(scores, axis=0), counts,
                      out=np.full(len(SUBJECTS), np.nan), where=counts > 0)
    squared_deviations = (scores - means) ** 2
    variances = np.divide(np.nansum(squared_deviations, axis=0), counts,
                          out=np.full(len(SUBJECTS), np.nan), where=counts > 0)
    stds = np.sqrt(variances)  # 本例描述整批資料，採 ddof=0。
    z_scores = np.divide(scores - means, stds,
                         out=np.full_like(scores, np.nan), where=stds > 0)
    # 零變異科目：有效分數 z 設 0，缺失格仍為 NaN。
    z_scores = np.where(valid & (stds == 0), 0.0, z_scores)

    # 正式成績只採完整列；不完整列不產生排名。
    complete = valid.all(axis=1)
    weighted = np.full(len(raw), np.nan)
    weighted[complete] = (scores[complete] * WEIGHTS).sum(axis=1)
    ranks = np.full(len(raw), np.nan)
    keys = np.round(weighted[complete], 6)
    ranks[complete] = 1 + (keys[None, :] > keys[:, None]).sum(axis=1)

    identity = raw[["學號", "姓名"]].reset_index(drop=True)
    cleaned = pd.concat([identity, pd.DataFrame(scores, columns=SUBJECTS)], axis=1)
    report = cleaned.copy()
    report["有效科數"] = valid.sum(axis=1)
    report["狀態"] = np.where(complete, "可計算", "待補資料")
    report["加權成績"] = weighted
    report["名次"] = pd.array(ranks, dtype="Int64")
    report = report.sort_values("加權成績", ascending=False, na_position="last", kind="stable")
    notes = np.where(counts == 0, "無有效資料，保留缺失",
                     np.where(stds == 0, "零變異：有效紀錄 z 設 0", "依公式計算"))
    summary = pd.DataFrame({"科目": SUBJECTS, "有效筆數": counts,
                            "缺失或無效筆數": len(raw) - counts,
                            "平均": means, "標準差": stds, "標準化說明": notes})
    z_report = pd.concat([identity, pd.DataFrame(z_scores, columns=SUBJECTS)], axis=1)
    # 補值僅供比較，與正式成績分檔；全缺失科目依舊無法補。
    imputed = np.where(valid, scores, means)
    trial = pd.concat([identity, pd.DataFrame(imputed, columns=SUBJECTS)], axis=1)
    trial["是否曾補值"] = (~valid).any(axis=1)
    trial["用途"] = "平均補值試算，不作正式排名"

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    tables = {
        "scores_cleaned.csv": cleaned,
        "scores_quality.csv": pd.DataFrame(issues, columns=["學號", "科目", "原始值", "問題"]),
        "scores_report.csv": report,
        "scores_subject_summary.csv": summary,
        "scores_z_scores.csv": z_report,
        "scores_imputation_trial.csv": trial,
    }
    for filename, table in tables.items():
        table.to_csv(output_dir / filename, index=False, encoding="utf-8-sig", float_format="%.2f")
    # npy 保留陣列型態、形狀與未四捨五入的數值，欄名另由文件維護。
    np.save(output_dir / "scores_cleaned.npy", scores)
    np.save(output_dir / "scores_z_scores.npy", z_scores)
    print("有效科目筆數：", counts)
    print("需查核格數：", len(issues))
    print(report.to_string(index=False))
    print("輸出位置：", output_dir)
    return {"scores": scores, "counts": counts, "means": means, "stds": stds,
            "weighted": weighted, "ranks": ranks, "z_scores": z_scores}


if __name__ == "__main__":
    analyze(BASE / "numpy_datasets" / "student_scores.csv", OUTPUT)

# 折線圖教材輸出

本目錄由 [折線圖教材](../../Data_Visualization_src/折線圖_Line_Plot.ipynb) 的存檔範例產生，全部是虛構教學資料。

- `18_租屋用電報告.png`、`.svg`：Matplotlib 圖片交付示範。
- `28_早餐店品項分面.png`：各分店的品項銷量。
- `30_午餐選擇報告.png`、`30_午餐費用摘要.csv`：午餐比較專題。
- `36_分店總銷量同圖.png`、`36_分店總銷量分面.png`：分店練習解答。
- `previews/`：逐格執行時產生的完整圖表與總覽，Notebook 內也已嵌入圖表。

供教材維護者使用：在專案根目錄執行 `python Data_Visualization/build_line_plot_lesson.py` 可重建 Notebook 與 36 支獨立範例（會清除 Notebook 已執行輸出）；再執行 `python Data_Visualization/verify_line_plot_lesson.py` 逐格執行、嵌入輸出並驗證獨立範例。一般學員不需要執行這兩支維護程式。

驗證採非互動繪圖後端，檢查所有程式格與獨立範例是否成功執行；課堂使用 Notebook 時仍請選擇安裝相關套件的 Python Kernel。

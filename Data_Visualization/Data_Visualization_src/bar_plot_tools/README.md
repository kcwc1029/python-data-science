# 長條圖教材維護工具

學員直接閱讀 [Notebook](../../長條圖_Bar_Plot.ipynb) 或執行 [獨立範例](../bar_plot_examples/README.md)，不必執行本目錄程式。

從專案根目錄執行：

```powershell
.venv/Scripts/python.exe Data_Visualization/Data_Visualization_src/bar_plot_tools/build_lesson.py
.venv/Scripts/python.exe Data_Visualization/Data_Visualization_src/bar_plot_tools/verify_lesson.py
```

- `build_lesson.py`：重建 Notebook、自製 CSV、資料字典、36 支範例與工作單；會覆寫這些同名檔案，Notebook 輸出重設為未執行。
- `verify_lesson.py`：在共享命名空間由上至下執行 Notebook 程式格，以非互動後端嵌入圖形與文字結果；另以獨立 Python 程序執行每支範例並實際繪製畫布，檢查關鍵數值、相對連結與警告。

驗證不模擬瀏覽器的 Notebook 介面操作。文字與圖形結果、預覽、驗證記錄存於 `Data_Visualization_output/bar_plot/`。一般 Notebook 執行使用正常的 `plt.show()`，獨立檔執行也可正常開啟圖形視窗。

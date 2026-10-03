# 熱圖 Heatmap 職訓教材

開啟 [熱圖_Heatmap.ipynb](熱圖_Heatmap.ipynb)。全篇繁體中文，Matplotlib與Seaborn各10個生活例題，從高中程度算術、表格與色階開始說明。

## 內容與檔案

- `datasets/`：20份CSV與資料字典，全部為合成教學資料。
- `examples/`：20支主範例與`common.py`共用設定，檔名對應Notebook目錄。
- `solutions/`：20支隨堂練習解答、3支綜合實作。
- `outputs/`：主例及綜合實作PNG、交接報表、驗證摘要。
- `src/build_material.py`：教材產生來源；重新執行會覆寫本教材、範例與資料，並清空Notebook執行輸出。修改教材請同步修改此來源。
- `src/verify_material.py`：逐格執行Notebook、產生內嵌圖片、驗證統計量並執行獨立程式。

先執行環境設定，再逐例練習；每個主例都重新讀自己的CSV，練習接續主例變數。從終端機執行獨立範例，例如：

```powershell
python "examples/01_一週三餐，錢都花在哪裡.py"
```

請保留整個資料夾，不要只搬Notebook；資料路徑支援從本資料夾、examples、solutions或專案根目錄啟動。不需要網路資料，也沒有必須申請的帳號。

需要Python與numpy、pandas、matplotlib、seaborn。中文字型優先尋找Microsoft JhengHei、Noto Sans CJK TC、Noto Sans TC、PingFang TC等；找不到時請安裝字型並重啟核心。`sns.set_theme`先執行，再設定字型，避免樣式重設蓋掉中文字型。

## 教學內容

每例包含生活情境、資料單位、技術拆解、程式閱讀指引、可執行程式、判讀限制、練習與參考解答。另有參數速查、除錯表、四個課堂活動、分層學習路徑、三題綜合實作、教師提問及100分評量規準。

重點包括共享色階、發散色盤、缺值與零、離散狀態、月曆定位、不等距網格、對數色階、長表轉換、中位數與樣本數、分母與加權比例、相關非因果、同籃矩陣、列標準化、robust端點及有方向矩陣。最後完成含去重、數值檢查、待查表與CSV的早餐店交接報告。

## 驗證方式

執行 `python src/verify_material.py`。驗證使用非互動Agg後端，按順序實際執行所有程式格，擷取文字與PNG輸出，並執行20個範例、20個解答及3個綜合程式；另核對資料矩陣、色階、遮罩、手算與重要筆數。這不等同VS Code或Jupyter前端自動化測試。

實際套件版本、儲存格數與驗證結果見 [outputs/驗證摘要.json](outputs/驗證摘要.json)。若套件升級，請重新執行驗證並看圖。所有可重跑腳本只讀原始CSV、將結果寫入outputs；第20例查核後的修正保留在新報表與修正軌跡，不覆寫原始資料。

## 範例索引

| 編號 | 工具 | 生活問題 | CSV／獨立程式 |
|---|---|---|---|
| 01 | Matplotlib | 一週三餐，錢都花在哪裡 | [資料](datasets/01_一週三餐花費.csv) · [程式](examples/01_一週三餐，錢都花在哪裡.py) |
| 02 | Matplotlib | 午休買飯，顏色之外也要讀得出數字 | [資料](datasets/02_午休買飯等多久.csv) · [程式](examples/02_午休買飯，顏色之外也要讀得出數字.py) |
| 03 | Matplotlib | 洗衣店什麼時候比較不擠 | [資料](datasets/03_洗衣店避開尖峰.csv) · [程式](examples/03_洗衣店什麼時候比較不擠.py) |
| 04 | Matplotlib | 六月七月用電，兩張圖要用同一把尺 | [資料](datasets/04_冷氣用電前後.csv) · [程式](examples/04_六月七月用電，兩張圖要用同一把尺.py) |
| 05 | Matplotlib | 預算差額，零是有意義的中心 | [資料](datasets/05_家庭預算差額.csv) · [程式](examples/05_預算差額，零是有意義的中心.py) |
| 06 | Matplotlib | 沒有記到價格，不代表免費 | [資料](datasets/06_採買缺值不是免費.csv) · [程式](examples/06_沒有記到價格，不代表免費.py) |
| 07 | Matplotlib | 座位狀態不是越大越好 | [資料](datasets/07_自習室座位狀態.csv) · [程式](examples/07_座位狀態不是越大越好.py) |
| 08 | Matplotlib | 把九月記帳變成月曆 | [資料](datasets/08_九月每日花費.csv) · [程式](examples/08_把九月記帳變成月曆.py) |
| 09 | Matplotlib | 房間大小不同，格子也不能假裝一樣大 | [資料](datasets/09_房間溫度網格.csv) · [程式](examples/09_房間大小不同，格子也不能假裝一樣大.py) |
| 10 | Matplotlib | 銷量差一千倍，對數色階在做什麼 | [資料](datasets/10_賣場品項銷量差很大.csv) · [程式](examples/10_銷量差一千倍，對數色階在做什麼.py) |
| 11 | Seaborn | 早餐店的長表，如何變成一張熱圖 | [資料](datasets/11_早餐店長表轉熱圖.csv) · [程式](examples/11_早餐店的長表，如何變成一張熱圖.py) |
| 12 | Seaborn | 等待時間用什麼代表，還要看有幾筆 | [資料](datasets/12_取餐等待中位數.csv) · [程式](examples/12_等待時間用什麼代表，還要看有幾筆.py) |
| 13 | Seaborn | 支付次數多，不代表偏好比例高 | [資料](datasets/13_支付方式看比例.csv) · [程式](examples/13_支付次數多，不代表偏好比例高.py) |
| 14 | Seaborn | 外送遲到率，沒訂單的格子不是零風險 | [資料](datasets/14_外送遲到率的分母.csv) · [程式](examples/14_外送遲到率，沒訂單的格子不是零風險.py) |
| 15 | Seaborn | 生活紀錄一起升降，不代表互相造成 | [資料](datasets/15_生活紀錄相關性.csv) · [程式](examples/15_生活紀錄一起升降，不代表互相造成.py) |
| 16 | Seaborn | 咖啡和飯糰常一起買嗎 | [資料](datasets/16_超商購物籃.csv) · [程式](examples/16_咖啡和飯糰常一起買嗎.py) |
| 17 | Seaborn | 每台家電自己的高峰，與誰最耗電是兩回事 | [資料](datasets/17_家電自己的高低峰.csv) · [程式](examples/17_每台家電自己的高峰，與誰最耗電是兩回事.py) |
| 18 | Seaborn | 一筆500杯團購，其他格子都看不清了 | [資料](datasets/18_一次團購拉高色階.csv) · [程式](examples/18_一筆500杯團購，其他格子都看不清了.py) |
| 19 | Seaborn | 去程回程不一定一樣，不能隨便遮一半 | [資料](datasets/19_景點移動時間.csv) · [程式](examples/19_去程回程不一定一樣，不能隨便遮一半.py) |
| 20 | Seaborn | 早餐店交接：從原始紀錄做到可追查的報告 | [資料](datasets/20_早餐店交接原始紀錄.csv) · [程式](examples/20_早餐店交接：從原始紀錄做到可追查的報告.py) |

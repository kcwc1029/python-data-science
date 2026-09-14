# NumPy：從陣列到高效數值運算

- [01 認識 NumPy：一週餐費一起算](#section-01)
- [02 ndarray：一維、二維與多維陣列](#section-02)
- [03 建立陣列：從空白紀錄到固定間隔](#section-03)
- [04 查看陣列：先認識資料再運算](#section-04)
- [05 資料型態與轉換：數字外觀不等於數字](#section-05)
- [06 索引與切片：取出想看的時間區間](#section-06)
- [07 布林遮罩：把消費條件變成篩選器](#section-07)
- [08 修改陣列：view 與 copy](#section-08)
- [09 調整形狀：重新排版，不是重新排序](#section-09)
- [10 陣列合併與拆分](#section-10)
- [11 向量化：把共同規則寫一次](#section-11)
- [12 廣播機制：不同形狀如何配對](#section-12)
- [13 數學函式與條件運算](#section-13)
- [14 統計與聚合：平均以外還要看什麼](#section-14)
- [15 理解 axis：被彙整掉的是哪一軸](#section-15)
- [16 缺失值：沒有記錄不等於零](#section-16)
- [17 排序與唯一值：保留姓名與數字的配對](#section-17)
- [18 隨機資料：可重現的抽籤與模擬](#section-18)
- [19 NumPy 與 Pandas：標籤和位置的交接](#section-19)
- [20 完整實作：成績統計、排名與標準化](#section-20)

- [跨節練習與驗收](./numpy_練習.md)
- [資料素材說明](./numpy_datasets/README.md)

## 認識 NumPy：一週餐費一起算

下班買便當、早餐店加蛋、下午買飲料，一筆金額不難算；如果要把整週、整班或整家店的數字一起調整，反覆寫加減乘除就容易漏掉。NumPy 適合讓「同一條計算規則」作用在一整批數值上。

`import numpy as np` 是載入套件並取簡稱；`np` 是慣例，不是 Python 關鍵字。`np.array(...)` 把現有數值建立成陣列。`餐費 * 2` 的意思要看餐費是哪一種物件：List 重複內容，數值陣列則讓每個數字乘二。這叫「逐元素運算」，元素就是其中一格的值。

| 工具      | 適合情境                         | 需要留意                           |
| --------- | -------------------------------- | ---------------------------------- |
| List      | 購物項目、少量混合資料           | 乘法可能是重複，不是金額翻倍       |
| ndarray   | 同一批價格、成績、數量做相同運算 | 主要依位置配對，自己維護位置的意義 |
| DataFrame | 有姓名、日期、類別的表格         | 運算可能按標籤對齊                 |

NumPy 常能把大量數值運算交給底層實作，減少 Python 逐次執行迴圈的負擔。但小資料、轉換成本、複雜文字處理都可能讓它沒有速度優勢；先追求計算正確與可讀性，不要把「用了 NumPy」當作一定比較快。

### 完整範例

## 從這裡開始

## 05 資料型態與轉換：數字外觀不等於數字

CSV 或表單讀入的「120」可能是文字。文字能顯示數字，卻不代表能直接拿來做數值運算。`astype(float)` 像把每一格重新登記成可運算的小數，預設會建立轉換後的陣列，必須接住回傳值。

整數只能存完整的單位，小數型態適合溫度、用電等。把 99.9 轉成整數不是四捨五入，而是往零截去小數，所以 -3.8 會變 -3。若直接把小數指定到整數陣列，也可能失去小數部分；計算折扣前就要選對型態。

常見數值陣列使用固定大小型態。`int8` 範圍只有 -128 到 127，不適合一般價格；不要為了省一點空間任意選很小的型態。浮點數則像有限位數的量尺，有些十進位小數不能精確表示。比較運算結果時可用 `np.isclose`，不要一律要求 `==`。

本教材的折扣是算術練習。若金額要求以元或分精確結算，要另外訂定取整規則；可以用最小貨幣單位的整數儲存，而不是靠畫面顯示兩位小數就認定數值完全精確。`np.round` 遇到正好一半採用靠近偶數的規則，也不等於所有商店的結帳規則。

### 完整範例

檔案：[05\_團購價格的型態轉換.py](./numpy_src/05_團購價格的型態轉換.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/05_團購價格的型態轉換.py
```

```python
import numpy as np

# 字串中的純數字可轉為浮點數；「待確認」則不能直接 astype。
price_text = np.array(["120", "85.5", "99.9"])
prices = price_text.astype(float)
print("九折：", prices * 0.9)
print("截去小數：", np.array([3.8, -3.8]).astype(int))
# 先轉浮點數，才能保留修改後的小數。
editable = np.array([100, 200]).astype(float)
editable[0] = 89.5
print("修改後：", editable)
print("浮點比較：", np.isclose(0.1 + 0.2, 0.3))
print("取最近偶數：", np.round([2.5, 3.5]))
```

### 輸出怎麼看

截去小數為 [3, -3]；editable 保留 89.5；isclose 是 True；round 結果是 [2, 4]。

### 課堂提問與動手練習

價格文字中有「售完」，直接 astype(float) 會如何？應先決定什麼？

<details>
<summary>展開參考解答與講師提醒</summary>

會發生 ValueError。先判斷它是缺失、停售狀態或錯誤輸入，不能未經判斷改成 0 元。

</details>

<a id="section-06"></a>

## 06 索引與切片：取出想看的時間區間

索引像座位號碼，用來找到一格；Python 從 0 開始編號，最後一個可用 -1。切片則取一段，格式是 `[開始:停止:步長]`，包含開始、不包含停止。這讓 `a[0:3]` 很自然地拿到三個位置：0、1、2。

二維資料用 `[列, 欄]`。`a[:, 0]` 表示全部列、第一欄；`a[0, :]` 表示第一列、全部欄。冒號單獨出現就是該軸全部選取。以單一整數索引某軸時，那一軸會消失，所以選一欄常得到一維資料。

若要保留二維，可用 `a[:, 0:1]`。這不是文字寫法上的小差異：`(5,)` 和 `(5, 1)` 在廣播時可能代表不同配對。初學者先練習每次選取後印出 shape。

超出範圍的單一索引會報錯；切片的終點超出範圍通常會截到邊界，不一定報錯。另請記住：NumPy 基本切片通常共用原資料，後面會專門示範修改造成的影響。

### 完整範例

檔案：[06\_通勤時間的索引切片.py](./numpy_src/06_通勤時間的索引切片.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/06_通勤時間的索引切片.py
```

```python
import numpy as np

# 列為週一到週五，欄為去程與回程，單位分鐘。
commute = np.array([[30, 35], [28, 40], [32, 33], [45, 50], [29, 31]])
print("週三回程：", commute[2, 1])
print("最後一天：", commute[-1])
print("前三天：\n", commute[:3])
print("所有去程：", commute[:, 0])
print("去程保留二維：", commute[:, 0:1].shape)
print("隔天觀察：\n", commute[::2])
```

### 輸出怎麼看

週三回程 33；所有去程 shape 為 (5,)，保留二維後為 (5, 1)。

### 課堂提問與動手練習

如何取週二到週四的回程？請先寫出列索引與停止位置。

<details>
<summary>展開參考解答與講師提醒</summary>

commute[1:4, 1]，得到 [40, 33, 50]。停止位置 4 不包含。

</details>

<a id="section-07"></a>

## 07 布林遮罩：把消費條件變成篩選器

布林值只有 True、False。`prices > 100` 不是問「整個陣列是否大於 100」，而是對每格提問，得到長度相同的答案清單。把答案清單放回中括號，True 的位置就留下，False 的位置被排除，這份清單叫遮罩。

多個逐元素條件用 `&` 表示同時成立、`|` 表示至少一個成立、`~` 表示反向。每個比較式都加括號，例如 `(prices >= 80) & (prices <= 120)`。Python 的 `and`、`or` 是整體邏輯運算，不能直接代替陣列的逐格條件。

`mask.sum()` 可以算符合的筆數，因為加總時 True 算 1、False 算 0。`mask.any()` 問有沒有任何一筆成立；`mask.all()` 問是不是全部成立。空資料的 all 會是 True，若真實流程可能沒有資料，應另外檢查 size。

商品名稱與價格若分開存放，必須保持同一個順序，再套用相同遮罩。不然可能顯示 A 店的名字搭配 B 店的價格。篩選出的新陣列是複本，但 `prices[mask] = ...` 這種直接指定仍會修改原陣列。

### 完整範例

檔案：[07\_找出超支與優惠餐點.py](./numpy_src/07_找出超支與優惠餐點.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/07_找出超支與優惠餐點.py
```

```python
import numpy as np

names = np.array(["雞腿飯", "湯麵", "咖哩飯", "水餃", "排骨飯"])
prices = np.array([130, 75, 110, 80, 120])
# 兩個條件分別加括號，再逐格取交集。
mask = (prices >= 80) & (prices <= 120)
print("遮罩：", mask)
print("可選餐點：", names[mask])
print("對應價格：", prices[mask])
print("符合數量：", mask.sum())
print("是否有超過 125 元：", (prices > 125).any())
# 直接對原陣列的選定位置更新。
prices[prices > 120] -= 10
print("優惠後：", prices)
```

### 輸出怎麼看

符合餐點為咖哩飯、水餃、排骨飯，共三筆；雞腿飯優惠後為 120。

### 課堂提問與動手練習

找出「低於 80 或高於 120」的餐點，請用優惠前資料計算。

<details>
<summary>展開參考解答與講師提醒</summary>

使用 (prices < 80) | (prices > 120)，優惠前會選出雞腿飯、湯麵。注意執行時資料是否已被修改。

</details>

<a id="section-08"></a>

## 08 修改陣列：view 與 copy

你想試算週末折扣，先取前三項商品，再把價格降低，結果原價表也跟著變了。這是 NumPy 初學最常遇到的意外之一。問題不是減法，而是兩個變數是否共用底下那塊資料。

`b = a` 是兩個名字指向同一個物件；`b = a[:2]` 的 b 是一個新的陣列物件，但基本切片建立的 view 仍指向 a 的部分資料；`b = a[:2].copy()` 才會複製出獨立資料。可以把 view 想成同一張白板的不同觀察窗口，copy 則是重新抄到另一張白板。

`np.shares_memory(a, b)` 可協助確認是否共用資料。不要只看變數名稱不同，或只看 `a is b` 是 False，就認為可以放心修改。整數陣列索引、布林索引取得的結果是 copy；基本切片是 view。對 numeric 陣列使用 copy，可以讓本課程的試算彼此獨立。

這個觀念也解釋了為何切片常有效率：只建立查看方式，不必先複製整批數字。代價是需要管理修改的影響。要保留原始資料、比較多種方案時，明確使用 copy，能讓教學與除錯更容易。

### 完整範例

檔案：[08\_試算折扣不要改到原價.py](./numpy_src/08_試算折扣不要改到原價.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/08_試算折扣不要改到原價.py
```

```python
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
```

### 輸出怎麼看

原資料變為 [90, 120, 150, 180]；trial 是 [100, 1]，修改 trial 不影響原資料。

### 課堂提問與動手練習

請先不執行：a=np.array([1,2,3])；b=a[1:]；b[:]=9。a 是什麼？如何避免？

<details>
<summary>展開參考解答與講師提醒</summary>

a 會變成 [1,9,9]。若要保留原資料，建立 b 時用 a[1:].copy()。

</details>

<a id="section-09"></a>

## 09 調整形狀：重新排版，不是重新排序

收集十四天的餐費後，想排成「兩週，每週七天」，這是改變看資料的形狀。`reshape` 不會增加或減少元素，也不會自動依星期或日期分類；它按指定順序把現有數值重新安排。

十四格可以變成 `(2, 7)`、`(7, 2)`，不能變成 `(3, 5)`。`reshape(2, -1)` 的 -1 表示讓 NumPy 依總格數推算該軸長度，只能有一個未知軸。這裡的 -1 跟索引的「最後一格」是不同語境。

`ravel()` 把陣列攤成一維，能共用記憶體時盡量回傳 view，必要時才複製；`flatten()` 則建立複本。`reshape` 也不保證一定共用資料，所以若後續修改不能影響原資料，就明確加上 `.copy()`。

二維 `transpose()` 或 `.T` 交換列欄：原本每列是一週，交換後每列是同一星期幾的兩週資料。它不是排序，也不是只把畫面轉過來。一維的 `.T` 仍是一維；若要直欄，使用 `reshape(-1, 1)`。三維以上可以指定軸順序，但本節先把二維練熟。

### 完整範例

檔案：[09\_兩週餐費重新排表.py](./numpy_src/09_兩週餐費重新排表.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/09_兩週餐費重新排表.py
```

```python
import numpy as np

# 十四天依日期先後存放的餐費。
costs = np.arange(80, 220, 10)
weeks = costs.reshape(2, 7)
print("兩週：\n", weeks)
print("推算欄數：", costs.reshape(2, -1).shape)
print("同星期跨週比較：\n", weeks.T)
print("攤平：", weeks.ravel())
print("一維轉置：", costs.T.shape)
print("真正直欄：", costs.reshape(-1, 1).shape)
# 若要一份可以任意修改的排版結果，明確複製。
independent = weeks.T.copy()
independent[0, 0] = 0
print("原餐費仍是：", costs[0])
```

### 輸出怎麼看

weeks 為 (2,7)、weeks.T 為 (7,2)；一維轉置仍是 (14,)，直欄為 (14,1)。

### 課堂提問與動手練習

24 筆每小時用電想分成四段時段，每段六小時，如何 reshape？這能自動校正缺漏的小時嗎？

<details>
<summary>展開參考解答與講師提醒</summary>

usage.reshape(4,6)。不能校正缺漏，必須先確認資料有依時間排列而且每小時一筆。

</details>

<a id="section-10"></a>

## 10 陣列合併與拆分

合併前先決定：要沿原有方向延長，還是新增一個分類方向？`concatenate` 沿已有的軸接起來；`stack` 新增一個軸。兩份 `(2, 3)` 表格沿 axis=0 接起來是 `(4, 3)`，沿 axis=1 是 `(2, 6)`；stack 沿新 axis=0 則是 `(2, 2, 3)`。

假設列代表兩天、欄代表三種商品，早班和晚班要保留班別，就可以 stack 成「班別 × 日期 × 商品」。如果只是把兩天接到另外兩天後面，才適合沿列 concatenate。陣列不會自動產生「早班」標籤，這些意義要另行保留。

沿某軸合併時，其他軸長度必須一致，因為拼接後仍要是規則表格。`split(a, 3)` 要求該軸能平均分三份；不能整除時用 `array_split`，它允許各份筆數不完全相同。拆出的部分可能共用原資料，修改前要想起上一節的 copy。

反覆在迴圈內 concatenate 通常會反覆配置與複製資料。若要逐筆收集，先累積到 Python List，再一次建立陣列通常比較合適。

### 完整範例

檔案：[10\_早晚班銷量接在一起.py](./numpy_src/10_早晚班銷量接在一起.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/10_早晚班銷量接在一起.py
```

```python
import numpy as np

morning = np.array([[10, 20, 30], [15, 25, 35]])
evening = np.array([[8, 12, 16], [9, 13, 17]])
print("沿列接：", np.concatenate([morning, evening], axis=0).shape)
print("沿欄接：", np.concatenate([morning, evening], axis=1).shape)
# 新增班別軸，保留兩張表的身分。
by_shift = np.stack([morning, evening], axis=0)
print("班別、日期、商品：", by_shift.shape)
# 十個號碼分給三組，不必每組一樣多。
for number, group in enumerate(np.array_split(np.arange(1, 11), 3), start=1):
    print(f"第 {number} 組：", group)
```

### 輸出怎麼看

合併形狀為 (4,3)、(2,6)、(2,2,3)；分組筆數為 4、3、3。

### 課堂提問與動手練習

兩份各七天的步數都是 shape=(7,)，想比較兩人的每日步數，如何變成 (2,7)？

<details>
<summary>展開參考解答與講師提醒</summary>

np.stack([person_a, person_b], axis=0)。concatenate 會變成 (14,)，失去獨立的人別軸。

</details>

<a id="section-11"></a>

## 11 向量化：把共同規則寫一次

向量化的起點不是背一個新函式，而是把「對每一筆做相同的事」寫成整批運算。例如每個人各買不同份數的便當，先用單價乘份數，再一起加包裝費。

`price * quantity` 是位置對位置相乘，第一格配第一格，第二格配第二格。這不會像 Pandas 那樣按照商品名稱自動對齊，所以必須確認兩個陣列的商品順序相同。`*` 是逐元素乘法，並不是矩陣乘法。

寫成 `(price * quantity).sum()`，先產生每種商品的小計，再加成訂單總額。這個順序和手算表格一致，適合用來檢查程式。NumPy 運算常產生中間陣列；面對很大的資料時，速度與記憶體都要考量。

不是看不到 for 就一定很快。像 `np.vectorize` 主要提供呼叫便利性，不應當作自動加速器。本課程先學原生陣列運算；若學生問為什麼不用迴圈，可以先展示相同答案，再討論大量數據時減少 Python 逐次工作的價值。

### 完整範例

檔案：[11\_團購總價與運費試算.py](./numpy_src/11_團購總價與運費試算.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/11_團購總價與運費試算.py
```

```python
import numpy as np

prices = np.array([90, 110, 80])
quantities = np.array([2, 1, 3])
# 先用熟悉的方式算，作為對照。
loop_total = 0
for price, quantity in zip(prices, quantities):
    loop_total += price * quantity
# 向量化保留每項小計，方便對帳。
subtotals = prices * quantities
print("各項小計：", subtotals)
print("迴圈總額：", loop_total)
print("陣列總額：", subtotals.sum())
# 本例假設每份收 5 元包裝費，並非每種商品只收一次。
print("含包裝費：", ((prices + 5) * quantities).sum())
```

### 輸出怎麼看

小計 [180,110,240]，總額 530；六份餐點包裝費共 30，含包裝費 560。

### 課堂提問與動手練習

若改成整筆訂單只收一次 30 元運費，公式應該放在哪裡？

<details>
<summary>展開參考解答與講師提醒</summary>

(prices \* quantities).sum() + 30。不能在每個商品小計都加 30，否則會重複收費。

</details>

<a id="section-12"></a>

## 12 廣播機制：不同形狀如何配對

三戶家庭各買兩種商品，數量表是 `(3, 2)`，兩種商品單價只有 `(2,)`。不必把價格手動抄成三列，NumPy 能把這兩個單價套用到每戶對應商品，這種配對規則叫 broadcasting，中文常稱廣播。

判斷規則是從 shape 的最右邊開始比較：對應長度相同，或其中一邊為 1，就能相容；缺少的左側軸視同長度 1。不符合就報錯。廣播是計算時的配對方式，不代表事先真的把價格複製了三份。

```text
數量表        (3, 2)
商品單價         (2,)  → 想成 (1, 2)
結果          (3, 2)

數量表        (3, 2)
每戶折扣      (3, 1)
結果          (3, 2)
```

為什麼每戶折扣 `(3,)` 不能直接乘 `(3,2)`？因為從右邊比，3 和 2 不相容。要讓每戶的折扣跨過商品欄，就把折扣排成 `(3,1)`。`discounts[:, None]` 也能加一個軸；初學時先用 `reshape(-1,1)` 比較直覺。

更危險的是表格剛好為 `(3,3)`：錯用 `(3,)` 可能不報錯，卻把折扣套到商品欄而非家庭列。程式成功不等於商業意義正確。每次廣播前，先寫出軸名稱和預期結果 shape。

### 完整範例

檔案：[12\_家庭採買與各戶折扣.py](./numpy_src/12_家庭採買與各戶折扣.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/12_家庭採買與各戶折扣.py
```

```python
import numpy as np

# 三戶家庭，兩欄分別是牛奶與雞蛋的購買數量。
quantities = np.array([[2, 1], [1, 3], [4, 2]])
prices = np.array([80, 60])
subtotals = quantities * prices  # (3,2) 配 (2,)。
# 每戶各自有一個折扣，要沿該戶的兩種商品套用。
discounts = np.array([0.9, 1.0, 0.8]).reshape(-1, 1)
discounted = subtotals * discounts
print("原小計：\n", subtotals)
print("折扣後小計：\n", discounted)
print("每戶應付：", discounted.sum(axis=1))
```

### 輸出怎麼看

每戶應付 [198,260,352]。以第一戶手算：(2×80+1×60)×0.9=198。

### 課堂提問與動手練習

shape=(7,3) 的七天三餐費用，要每天扣不同金額，七個折抵值應排成什麼形狀？

<details>
<summary>展開參考解答與講師提醒</summary>

(7,1)，讓每天一個值跨三欄套用。但先釐清優惠是每餐都扣，還是每日總額只扣一次；後者應先按日加總。

</details>

<a id="section-13"></a>

## 13 數學函式與條件運算

條件篩選會減少筆數，條件運算則常保留所有筆數，只改變每格結果。`np.where(條件, 成立時的值, 不成立時的值)` 很像對整欄套用試算表 IF。消費滿 500 免運，未滿收 60，就可以一次算完每筆訂單。

`np.clip(a, 下限, 上限)` 把低於下限的值拉到下限、高於上限的值壓到上限，範圍內不變。它適合「明確規定有上下限」的點數或試算規則；若原始成績出現 150，直接 clip 成 100 會掩蓋錯誤，資料清理應先辨認異常原因。

`abs` 看差距大小、不管正負；`sqrt` 取平方根；`floor` 往負無限方向取整；`ceil` 往正無限方向取整。以每箱六瓶來說，需要箱數可以用 ceil，七瓶不能只準備一箱。

`where` 不是逐筆延後執行的 if。Python 會先算好參數，所以 `np.where(b != 0, a / b, 0)` 仍可能先產生除以零警告。若要安全地有條件除法，可用 `np.divide` 的 out 與 where；out 先填好未計算位置的值。

### 完整範例

檔案：[13\_免運門檻與點數上限.py](./numpy_src/13_免運門檻與點數上限.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/13_免運門檻與點數上限.py
```

```python
import numpy as np

orders = np.array([320, 500, 780])
shipping = np.where(orders >= 500, 0, 60)
print("運費：", shipping)
print("應付：", orders + shipping)
print("點數限制：", np.clip(np.array([-5, 30, 150]), 0, 100))
print("箱數：", np.ceil(np.array([6, 7, 12]) / 6).astype(int))
print("和目標差距：", np.abs(orders - 500))
print("平方根：", np.sqrt(np.array([4, 9, 16])))
# 分母為零的會員暫無訂單，平均消費保留為 0。
count = np.array([2, 0, 3])
total = np.array([300, 0, 900])
average = np.divide(total, count, out=np.zeros(3), where=count != 0)
print("平均消費：", average)
```

### 輸出怎麼看

運費 [60,0,0]；箱數 [1,2,2]；平均消費 [150,0,300]。

### 課堂提問與動手練習

如果沒有訂單時應顯示「未知」而不是 0，out 可如何設定？

<details>
<summary>展開參考解答與講師提醒</summary>

out=np.full(3, np.nan)。零可能被誤認為確實免費，未知值應與已知的零分開。

</details>

<a id="section-14"></a>

## 14 統計與聚合：平均以外還要看什麼

同樣平均三十分鐘，一條路每天都差不多，另一條路有時十分鐘、有時五十分鐘，你會選哪一條？平均回答「大約多久」，標準差回答「上下起伏有多大」。統計不只是算出一個數字，而是協助做不同面向的判斷。

`sum` 加總、`mean` 平均、`min` 最小、`max` 最大。平均就是總和除以筆數。中位數 `median` 則是排序後的中間位置，較不容易被少數很大的值拉走，例如一週突然有一天計程車費特別高。

標準差可以分四步講：先求平均；每筆減平均，得到偏差；偏差平方再平均，避免正負互相抵消；最後開平方根，讓單位回到分鐘。對 [20,30,40]，平均 30，偏差 [-10,0,10]，平方平均 200/3，標準差約 8.16 分鐘。

`np.std` 預設 `ddof=0`，分母是 N，適合描述手上整批觀察值。`ddof=1` 使用 N-1，是常見的樣本標準差設定；只有一筆資料時不適用。不能只因「比較專業」就隨便改參數。本教材的成績專題描述整班資料，使用 ddof=0。

不要把「平均＋一個標準差」直接當作保證範圍或固定比例；還需要資料分布條件。最小值也不等於每天都能達成的時間。讓學生用自己的話描述結果，比背函式名稱更重要。

### 完整範例

檔案：[14\_兩條通勤路線哪條穩定.py](./numpy_src/14_兩條通勤路線哪條穩定.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/14_兩條通勤路線哪條穩定.py
```

```python
import numpy as np

route_a = np.array([28, 30, 32, 30, 30])
route_b = np.array([10, 20, 30, 40, 50])
for name, route in [("A 路線", route_a), ("B 路線", route_b)]:
    print(name, "總時間", route.sum(), "平均", route.mean())
    print("最短", route.min(), "最長", route.max(), "標準差", route.std())
# 手動拆開標準差計算，與 NumPy 比較。
values = np.array([20, 30, 40])
deviations = values - values.mean()
manual_std = np.sqrt((deviations ** 2).mean())
print("手算標準差：", manual_std)
print("NumPy 標準差：", values.std())
print("被大額拉高的平均：", np.mean([80, 90, 100, 110, 1000]))
print("中位數：", np.median([80, 90, 100, 110, 1000]))
```

### 輸出怎麼看

兩條路平均都是 30，但 A 標準差約 1.26、B 約 14.14。大額例子的平均 276，中位數 100。

### 課堂提問與動手練習

若上班不能遲到，只比較平均是否足夠？還想看什麼資料？

<details>
<summary>展開參考解答與講師提醒</summary>

不夠。可再看最大值、分位數、尖峰時段與樣本天數；本例 A 比較穩定，但五天不能代表所有未來情況。

</details>

<a id="section-15"></a>

## 15 理解 axis：被彙整掉的是哪一軸

`axis` 不是一個必須死背「橫或直」的口訣，而是指定要把哪個軸的不同位置彙整起來。假設資料 `(人數, 天數)`，axis=0 是人數軸，沿它加總後，人別被合在一起，留下每天的總費用；axis=1 是天數軸，彙整後留下每個人的總費用。

用形狀推理比用視覺方向更可靠：`(3,4)` 沿 axis=0 加總變 `(4,)`；沿 axis=1 變 `(3,)`；不指定 axis 則加總所有格子，變單一數值。三維也是同樣邏輯，不必重新發明口訣。

`keepdims=True` 不把被彙整軸完全拿掉，而是保留長度 1。`(3,4)` 沿 axis=1 平均並保留軸得到 `(3,1)`，這個形狀可以直接與原陣列廣播，計算每人每天距離自己平均多少。

課堂上可以畫一張三列四欄的表，用彩筆圈出「要合在一起的格子」，然後讓學生說結果中每一格代表什麼。若只會說 axis=0 是直向，追問：直向算完剩下的是人，還是天？

### 完整範例

檔案：[15\_三個人的一週餐費.py](./numpy_src/15_三個人的一週餐費.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/15_三個人的一週餐費.py
```

```python
import numpy as np

# 三個人、四天餐費。
costs = np.array([[80, 100, 120, 100], [90, 90, 90, 90], [100, 110, 120, 130]])
print("每天全體總額：", costs.sum(axis=0))
print("每人四天總額：", costs.sum(axis=1))
print("全部總額：", costs.sum())
personal_mean = costs.mean(axis=1, keepdims=True)
print("個人平均形狀：", personal_mean.shape)
print("各天與自己的平均差：\n", costs - personal_mean)
```

### 輸出怎麼看

每天總額 [270,300,330,320]；每人總額 [400,360,460]；全部 1220。

### 課堂提問與動手練習

三間店、七天、四種商品 shape=(3,7,4)，要算每間店整週每種商品總量，用哪個 axis？

<details>
<summary>展開參考解答與講師提醒</summary>

axis=1，彙整日期軸，結果 shape=(3,4)。如要每間店整週所有商品總量，可 sum(axis=(1,2))，結果 (3,)。

</details>

<a id="section-16"></a>

## 16 缺失值：沒有記錄不等於零

某天沒有填餐費，有兩種完全不同的可能：真的沒花錢，或只是忘記記帳。前者是 0，後者是未知。`np.nan` 可以表示浮點陣列中的缺失數值，但它不會告訴你為什麼缺失。

整數陣列不能直接容納浮點 NaN，通常需要先轉 float。判斷缺失使用 `np.isnan`，不要用 `a == np.nan`；NaN 甚至不等於它自己。一般 mean 遇到 NaN 會傳播成 NaN，提醒你這批資料不完整。

`nanmean` 忽略 NaN 後，用有效筆數當分母。已知 [100,120] 的平均是 110，不代表第三天也是 110。用平均補缺失是一種假設，可能低估波動程度。資料分析必須同時報告缺失量與採用的處理方法。

全部缺失的一欄沒有可用平均，直接 nanmean 會發出警告並得到 NaN；`nansum` 對全缺失會得到 0，也不能解讀成確實沒有消費。因此本例先計算有效筆數，再做有條件除法。`isfinite` 可同時排除 NaN 與正負無限大，nan 系列函式並不會自動忽略無限大。

### 完整範例

檔案：[16\_忘記記帳的那一天.py](./numpy_src/16_忘記記帳的那一天.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/16_忘記記帳的那一天.py
```

```python
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
```

### 輸出怎麼看

已知資料平均為 220/3≈73.33，因為 0 是有效資料；全缺失欄平均仍為 NaN。

### 課堂提問與動手練習

如果忘記記帳的都是聚餐日，直接用平日平均補值可能產生什麼偏差？

<details>
<summary>展開參考解答與講師提醒</summary>

可能低估真正花費。缺失不一定隨機，應回查紀錄、保留缺失標記，不能只為了讓表格沒有空格而補值。

</details>

<a id="section-17"></a>

## 17 排序與唯一值：保留姓名與數字的配對

`np.sort` 給你排序後的值；`np.argsort` 給你「依排序順序應該取哪些原位置」。如果只排序價格、不重新排列店名，畫面可能看似合理卻標錯店家。取得排序位置後，所有相關陣列都套同一份位置。

`np.sort(a)` 回傳排序後的複本，`a.sort()` 則修改 a 本身，回傳 None。不要寫 `a = a.sort()`，否則 a 最後會是 None。二維 sort 預設沿最後一軸排序，不會自動依其中一欄重排整張表。

`np.unique` 可以取得不重複類別，搭配 return_counts 計次；預設結果通常是排序後的唯一值，不是保留首次出現順序。若需要名稱標籤的彙整，Pandas 的 value_counts 也很適合。

排序位置不是名次。假設成績 [90,90,80]，本教材採競賽排名 1、1、3：一個人的名次等於「比他高分的人數＋1」。`argsort` 只能先排出順序，同分要不要同名次、下一名是 2 還是 3，需要自己定義。

### 完整範例

檔案：[17\_比價排序與同分名次.py](./numpy_src/17_比價排序與同分名次.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/17_比價排序與同分名次.py
```

```python
import numpy as np

shops = np.array(["巷口", "車站", "市場", "公司旁"])
prices = np.array([110, 95, 95, 120])
# stable 讓同價商品保留原先的先後順序。
order = np.argsort(prices, kind="stable")
print("排序位置：", order)
print("店名：", shops[order])
print("價格：", prices[order])
values, counts = np.unique(prices, return_counts=True)
print("價格種類：", values, "各有幾家：", counts)
# 小班級示範競賽排名；大型資料可改用更節省空間的方法。
scores = np.array([90, 90, 80])
ranks = 1 + (scores[None, :] > scores[:, None]).sum(axis=1)
print("同分同名次：", ranks)
```

### 輸出怎麼看

店家排序為車站、市場、巷口、公司旁；同分名次為 [1,1,3]。

### 課堂提問與動手練習

如何由高分排到低分，又讓同分維持原順序？

<details>
<summary>展開參考解答與講師提醒</summary>

對一般本例整數成績使用 np.argsort(-scores, kind="stable")。直接把升冪結果反轉，也會反轉同分者順序。

</details>

<a id="section-18"></a>

## 18 隨機資料：可重現的抽籤與模擬

隨機數可以用來製作練習資料、模擬可能情境、安排遊戲分組。這裡的「模擬」不是預測未來：你給什麼機率與分布假設，結果就反映那些假設，不會自動知道真實店家的生意。

`rng = np.random.default_rng(42)` 建立隨機數產生器。42 是種子，可以換成其他整數；它不是特別幸運的數字。在相同環境、相同種子與相同呼叫順序下，可以重現結果，方便老師與學生比對。

同一個 rng 連續呼叫時，內部狀態會前進，不會每次給一樣的資料。若在每次抽籤前都重新建立相同種子的產生器，就會一直拿到相同起點，不適合拿來假裝新的抽籤。跨 NumPy 版本不應無條件承諾亂數序列完全相同；保存版本與實際輸入更可靠。

`integers(20, 51)` 產生 20 到 50，51 不包含；`choice` 選人，replace=False 表示同一次抽選不重複；`permutation` 可以把全部人打亂。normal 產生的是連續數值，可能有負數，所以不能直接假裝所有分布都適合人數。

### 完整範例

檔案：[18\_抽籤與一週客流模擬.py](./numpy_src/18_抽籤與一週客流模擬.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/18_抽籤與一週客流模擬.py
```

```python
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
```

### 輸出怎麼看

兩份相同種子的第一批資料一致；客數落在 20 到 50；分享者同一批不重複。

### 課堂提問與動手練習

五人抽六個不重複名額會怎樣？應該改哪個需求？

<details>
<summary>展開參考解答與講師提醒</summary>

replace=False 且 size=6 會報錯。應減少名額、增加候選人，或明確允許重複，不能偷偷把規則改掉。

</details>

<a id="section-19"></a>

## 19 NumPy 與 Pandas：標籤和位置的交接

讀 CSV、辨認日期、處理商品名稱適合交給 Pandas；選出確定要算的數值欄，再用 NumPy 計算。`df[["單價", "份數"]].to_numpy()` 的欄位順序就是轉出後的位置順序，輸出陣列本身不會帶著欄名和 index。

不能把整張含姓名、備註的表直接轉換後，就期待每欄仍保有獨立數值型態。普通 ndarray 共用一種 dtype，混合欄位可能得到 object 陣列，數值計算更不直覺。先選數值欄，再明確指定 dtype。

`to_numpy(copy=True)` 適合本教材的獨立計算。不要假設預設 copy=False 一定沒有複製，也不要假設回傳值一定可以直接修改或修改後會回寫 DataFrame。Pandas 的型態轉換與資料共用規則可能影響結果，初學先選擇明確的複本。

最需要注意的是對齊：Pandas Series 相加通常依標籤，NumPy 陣列相加依位置。兩張表即使長度相同，姓名順序不同也不能直接把各自 to_numpy 的結果相加。應先在 Pandas 依明確鍵值 merge 或 reindex，確認順序後再轉換。

### 完整範例

檔案：[19\_便當訂單轉成數值陣列.py](./numpy_src/19_便當訂單轉成數值陣列.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/19_便當訂單轉成數值陣列.py
```

```python
from pathlib import Path
import numpy as np
import pandas as pd

# 從程式本身的位置找章節資料夾，避免受終端機所在目錄影響。
BASE = Path(__file__).resolve().parents[1]
output_dir = BASE / "numpy_outputs"
output_dir.mkdir(parents=True, exist_ok=True)
orders = pd.read_csv(BASE / "numpy_datasets" / "lunch_orders.csv")
# 欄位順序固定為單價、份數，並使用獨立浮點數陣列。
values = orders[["單價", "份數"]].to_numpy(dtype=float, copy=True)
subtotals = values[:, 0] * values[:, 1]
report = orders.copy()
report["小計"] = subtotals
report.to_csv(output_dir / "lunch_report.csv", index=False, encoding="utf-8-sig")
print(report)
print("整筆訂單：", np.sum(subtotals))
# 示範標籤對齊與位置對齊的差異。
a = pd.Series([100, 200], index=["小安", "小美"])
b = pd.Series([20, 10], index=["小美", "小安"])
print("Pandas 按姓名：\n", a + b)
print("NumPy 按位置：", a.to_numpy() + b.to_numpy())
```

### 輸出怎麼看

訂單總額 530；Pandas 中小安 110、小美 220；直接按位置相加是 [120,210]。

### 課堂提問與動手練習

要讓 NumPy 相加也正確，b 應先如何排列？

<details>
<summary>展開參考解答與講師提醒</summary>

先用 b.reindex(a.index)，確認沒有缺失標籤，再 to_numpy。正式資料若姓名不唯一，應改用可靠的識別碼。

</details>

<a id="section-20"></a>

## 20 完整實作：成績統計、排名與標準化

這個專題回答四個問題：每科表現如何？每位學生的加權成績是多少？缺考或輸入錯誤會影響哪些結果？不同科目的分數，如何換成相對於班級平均的位置？資料是虛構職訓班的餐飲實作、服務溝通、安全衛生分數，不涉及真實個資。

### 先定分析規則，再寫公式

原始檔每列一位學生，以學號識別，三科應介於 0 到 100。姓名只用於呈現，不當唯一鍵。空白視為缺失，非數字、無限大和超出範圍的值都記入品質報告，再標成 NaN。缺失不等於零分，也不直接以 100 或 0 截斷異常值。

本例採「完整三科才能計算正式加權成績」；缺任一科者不列名次，標示待補資料。各科描述統計使用該科有效資料，所以每科樣本數可能不同。為教學比較，另外產生平均補值的試算表，但不拿它發正式成績。這是本專題明訂的規則，不代表所有學校都如此。

三科權重為 0.5、0.3、0.2，相加應為 1。若三科是 [80,70,100]，加權成績是 80×0.5＋70×0.3＋100×0.2＝80，不能再除以三。使用 `(scores * weights).sum(axis=1)`，先按科乘權重，再按人彙整各科。

### 標準化用高中程度怎麼解釋

假設某科平均 70、標準差 10，80 分比平均多 10 分，剛好多一個標準差；把它寫成 z 分數，就是 `(80-70)/10=1`。60 分是 -1，70 分是 0。公式 `z=(分數-該科平均)/該科標準差` 分兩步：先把平均移到零，再用標準差當新的尺。

z 分數沒有原本的「分」單位；它不是百分比，也不是名次。z=1 不代表贏過固定百分比的同學，除非另有分布假設。標準化也不會自動讓資料變成常態分布。它能描述在同一批資料中的相對位置，不能證明不同考試難度公平。

如果整班某科都 100 分，標準差是零，代表這批資料沒有差異，不能除以零。本例把該科有效紀錄的 z 設為 0，並在科目摘要寫出處理說明；缺失仍保留 NaN。若整科沒有有效值，平均、標準差、z 都維持 NaN，不憑空建立分數。

### 手算與形狀追蹤

| 階段                | 形狀  | 每個位置的意義           |
| ------------------- | ----- | ------------------------ |
| scores              | (8,3) | 學生 × 科目              |
| valid               | (8,3) | 該格是否有效             |
| counts、means、stds | (3,)  | 每科一個數值             |
| weights             | (3,)  | 每科一個權重             |
| scores \* weights   | (8,3) | 每位學生每科的加權部分   |
| weighted            | (8,)  | 每人正式加權總成績或 NaN |
| z_scores            | (8,3) | 每位學生各科相對位置     |

本例同分採競賽排名 1、1、3。排名前把加權成績四捨五入到六位小數作為比較鍵，避免浮點數極小誤差拆開本應同分者；報表顯示兩位小數。若實務規定「顯示到兩位就視為同分」，要相應改成兩位比較鍵。

### 程式閱讀順序

先看讀檔與資料檢查，再看 valid 遮罩。接著逐科統計有效數量；平均是有效總和除有效筆數，標準差只採有效格的偏差。最後才算加權、排名與輸出。請不要一開始就把整段程式背起來，每個階段都能對應前面的單節範例。

### 完整範例

檔案：[20\_成績統計與標準化.py](./numpy_src/20_成績統計與標準化.py)

```bash
# 在專案根目錄執行。
uv run python numpy/numpy_src/20_成績統計與標準化.py
```

```python
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
```

### 輸出怎麼看

主資料共八人，需查核四格。三科有效筆數 [7,5,8]。安全衛生全部有效值都為 100，標準差為 0。正式排名：S001 與 S008 同為 92 分並列第一，S006 為 90 分第三，S007 為 80 分第四，S002 為 71 分第五；其餘三人待補資料。

### 課堂提問與動手練習

先不補值：小芸服務溝通缺失，能否直接 nanmean 當正式加權成績？如果整科都缺失，應怎麼呈現？

<details>
<summary>展開參考解答與講師提醒</summary>

不能。nanmean 會改變分母且不會照三科權重計算，還改變了評分依據。依本例規則先標待補資料；整科缺失則報告有效筆數 0，平均與 z 保留 NaN。

</details>

## 21 專題報表如何驗收與閱讀

執行第 20 節後，開啟 `numpy_outputs`。先看品質報告，再看正式成績，不要只挑名次表看。

| 檔案                        | 用途                                       | 需要注意                             |
| --------------------------- | ------------------------------------------ | ------------------------------------ |
| scores_quality.csv          | 列出四格缺失或異常的學號、科目、原值、問題 | 是待回查清單，不是直接刪除學生的依據 |
| scores_cleaned.csv          | 無效分數改為空白的三科資料                 | 學號與姓名保留，原 CSV 不被改寫      |
| scores_subject_summary.csv  | 每科有效筆數、缺失量、平均、標準差與說明   | 有效筆數不同，不能只看平均           |
| scores_report.csv           | 正式加權成績、狀態與競賽名次               | 待補資料者留在表內，成績與名次空白   |
| scores_z_scores.csv         | 各科 z 分數                                | 正負是相對位置；安全衛生有效值設零   |
| scores_imputation_trial.csv | 各科平均補值試算                           | 明確標示用途，不作正式成績           |
| scores_cleaned.npy          | 清理後數值矩陣                             | 保留 shape 與 dtype，不含姓名欄名    |
| scores_z_scores.npy         | 未四捨五入的 z 矩陣                        | 適合重新載入作計算                   |

CSV 的數值顯示到兩位小數，重新讀入 CSV 可能失去更多小數精度；要繼續精確比較，使用 npy 或重新跑分析。`.npy` 是 NumPy 的二進位陣列格式，不能當文字檔閱讀。可在 Python 使用 `np.load(檔案路徑, allow_pickle=False)` 讀取本教材的純數值檔。

import numpy as np
import pandas as pd

# 1. 用 list 建立原始資料 (包含 None)
data = [120, 80, None, 60, 95, None, 110]

# 2. 建立 stock1 (Pandas Series，無自訂索引)
stock1 = pd.Series(data)

# 3. 加入索引建立 stock2
index_labels = ["Apple", "Banana", "Orange", "Mango", "Grape", "Peach", "Melon"]
stock2 = pd.Series(data, index=index_labels)

# 4. 將 stock2 轉為字典 stock3
stock3 = stock2.to_dict()

# --- 輸出結果 ---

print("stock1")
print(stock1)
print("\nstock2")
print(stock2)
print("\nstock3")
print(stock3)

# 輸出 Banana 的庫存值
print(f"\nBanana 庫存： {stock2['Banana']}")

# 檢查缺失值與計算數量
print("\n缺失值檢查：")
print(stock2.isnull())
print(f"\n缺失值數量： {stock2.isnull().sum()}")

# 5. 將 stock2 存檔為 0520_stock.csv
stock2.to_csv("0520_stock.csv", header=False)

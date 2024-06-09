import pandas as pd

# 讀取原始 CSV 檔案
df = pd.read_csv('sidewalk_point.csv', header=None)

# 創建一個空的列表來存儲結果
results = []

# 處理每一列數據
for idx, row in df.iterrows():
    row_data = row.dropna().tolist()  # 移除空值並轉換為列表
    for i in range(0, len(row_data), 2):
        new_row = [idx + 1] + row_data[i:i + 2]  # 添加原列編號和兩個數據
        results.append(new_row)

# 將結果轉換為 DataFrame
result_df = pd.DataFrame(results, columns=[0, 1, 2])

# 將結果寫回新的 CSV 檔案
result_df.to_csv('sidewalk_point.csv', index=False, header=False)

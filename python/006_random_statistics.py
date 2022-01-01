# 1. python 亂數模組
# 隨機選取
import random

# 從列表中隨機選取一個資料
random.choice([0, 1, 5, 8])

# 從列表中隨機選取兩個資料
random.sample([0, 1, 5, 8], 2)

# 列表隨機調換順序
data = [0, 1, 5, 8]
random.shuffle(data)
print(data)

# 隨機亂數
random.random()
random.uniform(0.0, 1.0) # 取得 0.0~1.0 之間的隨機亂數

# 常態分配亂數，取得平均數 100, 標準差 10
random.normalvariate(100, 10)

# 2. python 統計模組
import statistics as stat
stat.mean([1, 4, 6, 9])
stat.median([1, 4, 6, 9])
stat.stdev([1, 4, 6, 9])

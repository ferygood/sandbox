# 實體物件的建立與應用
class File:
  # 初始化函式
  def __init__(self, name):
    self.name = name
    self.file = None #尚未開啟檔案，初期是 None
  # 實體方法
  def open(self):
    self.file = open(self.name, mode="r", encoding="utf-8")
  def read(self):
    return self.file.read()
  
# 讀取檔案
f = File("data.txt")
f.open()
data = f.read()
print(data)

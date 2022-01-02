# 基礎環境建置範例
from flask import Flask
app = Flask(__name__) # __name__ 代表目前執行的模組

@app.route("/") #函式的裝飾 (Decorator): 以函式為基礎，提供附加的功能
def home():
    return "This is my HomePage!"

@app.route("/about")
def about():
    return "About the author:"
  
if __name__ == "__main__": # 如果 app.py 當作主程式執行
    app.run() # 立刻啟動伺服器

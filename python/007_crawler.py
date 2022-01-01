# 1. 網路連線
import urllib.request as request
src = "https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
  data = response.read().decode("utf-8") #取得台大網站原始碼
print(data)



# 2. 串接，擷取公開資料、將公司名稱列表寫入檔案
import urllib.request as request
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
  data = json.load(response) #利用 json 模組處理

clist = data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
  for company in clist:
    file.write(company["公司名稱"] + "\n")


    
# 3. 網路爬蟲 Web Crawler (盡可能模仿一般使用者)
# 抓取 ptt 網頁原始碼
import urllib.request as req
import bs4
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件並附加 Request Headers 的資訊
request = req.Request(url, headers = {
  "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
})
with req.urlopen(request) as response:
  data = response.read().decode("utf-8")
# 解析原始碼取得文章標題
root = bs4.BeautifulSoup(data, "html.parser") #讓 BeautifulSoup 協助我們解析 HTML 格式文件
titles = root.find_all("div", class_="title") #尋找所有 class="title"的 div 標籤
for title in titles:
  if title.a != None: #如果標題包含 a 標籤（沒有被刪除), 印出來
    print(title.a.string)
    
    
    
    
# 4. Cookie (網站存放在瀏覽器的一小段內容，在連線的時候放在 Reuquest Headers 中送出)
# 解析頁面的超連結，並連續抓取頁面
# 例子：八卦版 over 18
import urllib.request as req
import bs4

def getData():
  # 建立一個 Request 物件並附加 Request Headers 的資訊，新增 cookie 資訊來抓取頁面(按過滿 18 歲)
  request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "cookie":"over18=1"
  })
  with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
  # 解析原始碼取得文章標題
  root = bs4.BeautifulSoup(data, "html.parser") #讓 BeautifulSoup 協助我們解析 HTML 格式文件
  titles = root.find_all("div", class_="title") #尋找所有 class="title"的 div 標籤
  for title in titles:
    if title.a != None: #如果標題包含 a 標籤（沒有被刪除), 印出來
      print(title.a.string)
  # 想抓多頁，所以要抓取上一頁的連結
  nextLink = root.find("a", string="‹ 上頁") # 找到內文是 ‹ 上頁 的標籤
  return nextLink["href"]

# 抓取多頁的標題
# 因為每一頁的上一頁的網址不同，所以要用程式動態去抓
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
  pageURL="https://www.ptt.cc"+getData(pageURL)
  count+=1


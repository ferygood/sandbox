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

  
  
  
# 5. AJAX/XHR 網站技術分析
# 認出網站運作模式，找出真正能抓到資料的網址，以 medium.com 為例
# 可用開發者工具看 Network --> XHR 分析
import urllib.request as reqjson
import json
url = "https://medium.com/_/api/home-feed"
request = req.Request(url, headers = {
  "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
})
with req.urlopen(request) as response:
  data = response.read().decode("utf-8")
# 解析 JSON 
data = data.replace("])}while(1);</x>","")
data = json.loads(data)
# 取得資料中的文章標題
posts = data["payload"]["references"]["Post"]
for key in posts:
  post = posts[key]
  print(post["title"])

  
  
  

  
# 6. Request Data (以新版 medium.com 為例)
# Request Payload: 帶上額外附加的資訊來成功發送請求
import urllib.request as req
import json
url = "https://medium.com/_/graphql"
requestData = {"operationName":"TopicHandlerHomeFeed","variables":{"topicSlug":"editors-picks","feedPagingOptions":{"limit":25,"to":"1640873708476"}},"query":"query TopicHandlerHomeFeed($topicSlug: ID!, $feedPagingOptions: PagingOptions) {\n  topic(slug: $topicSlug) {\n    ...TopicHandlerHomeFeed_topic\n    __typename\n  }\n}\n\nfragment TopicHandlerHomeFeed_topic on Topic {\n  id\n  name\n  latestPosts(paging: $feedPagingOptions) {\n    postPreviews {\n      ...TopicHandlerHomeFeed_postPreview\n      __typename\n    }\n    pagingInfo {\n      next {\n        limit\n        to\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment TopicHandlerHomeFeed_postPreview on PostPreview {\n  postId\n  post {\n    id\n    ...HomeFeedItem_post\n    __typename\n  }\n  __typename\n}\n\nfragment HomeFeedItem_post on Post {\n  __typename\n  id\n  title\n  firstPublishedAt\n  mediumUrl\n  collection {\n    id\n    name\n    domain\n    logo {\n      id\n      __typename\n    }\n    __typename\n  }\n  creator {\n    id\n    name\n    username\n    imageId\n    mediumMemberAt\n    __typename\n  }\n  previewImage {\n    id\n    __typename\n  }\n  previewContent {\n    subtitle\n    __typename\n  }\n  readingTime\n  tags {\n    ...TopicPill_tag\n    __typename\n  }\n  ...BookmarkButton_post\n  ...CreatorActionOverflowPopover_post\n  ...PostPresentationTracker_post\n  ...PostPreviewAvatar_post\n}\n\nfragment TopicPill_tag on Tag {\n  __typename\n  id\n  displayTitle\n}\n\nfragment BookmarkButton_post on Post {\n  visibility\n  ...SusiClickable_post\n  ...AddToCatalogBookmarkButton_post\n  __typename\n  id\n}\n\nfragment SusiClickable_post on Post {\n  id\n  mediumUrl\n  ...SusiContainer_post\n  __typename\n}\n\nfragment SusiContainer_post on Post {\n  id\n  __typename\n}\n\nfragment AddToCatalogBookmarkButton_post on Post {\n  ...AddToCatalogBase_post\n  __typename\n  id\n}\n\nfragment AddToCatalogBase_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        catalogItemIds\n        __typename\n      }\n      predefinedContainingThis {\n        catalogId\n        predefined\n        catalogItemIds\n        __typename\n      }\n      __typename\n    }\n    ...editCatalogItemsMutation_postViewerEdge\n    ...useAddItemToPredefinedCatalog_postViewerEdge\n    __typename\n    id\n  }\n  ...WithToggleInsideCatalog_post\n  __typename\n}\n\nfragment editCatalogItemsMutation_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    catalogsContainingThis(type: LISTS) {\n      catalogId\n      version\n      catalogItemIds\n      __typename\n    }\n    predefinedContainingThis {\n      catalogId\n      predefined\n      version\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment useAddItemToPredefinedCatalog_postViewerEdge on PostViewerEdge {\n  id\n  catalogsConnection {\n    predefinedContainingThis {\n      catalogId\n      version\n      predefined\n      catalogItemIds\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment WithToggleInsideCatalog_post on Post {\n  id\n  viewerEdge {\n    catalogsConnection {\n      catalogsContainingThis(type: LISTS) {\n        catalogId\n        __typename\n      }\n      predefinedContainingThis {\n        predefined\n        __typename\n      }\n      __typename\n    }\n    __typename\n    id\n  }\n  __typename\n}\n\nfragment CreatorActionOverflowPopover_post on Post {\n  allowResponses\n  id\n  statusForCollection\n  isLocked\n  isPublished\n  clapCount\n  mediumUrl\n  pinnedAt\n  pinnedByCreatorAt\n  curationEligibleAt\n  mediumUrl\n  responseDistribution\n  visibility\n  ...useIsPinnedInContext_post\n  pendingCollection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    __typename\n  }\n  creator {\n    id\n    ...MutePopoverOptions_creator\n    ...auroraHooks_publisher\n    __typename\n  }\n  collection {\n    id\n    name\n    creator {\n      id\n      __typename\n    }\n    avatar {\n      id\n      __typename\n    }\n    domain\n    slug\n    ...MutePopoverOptions_collection\n    ...auroraHooks_publisher\n    __typename\n  }\n  ...ClapMutation_post\n  ...NewsletterV3EmailToSubscribersMenuItem_post\n  __typename\n}\n\nfragment useIsPinnedInContext_post on Post {\n  id\n  collection {\n    id\n    __typename\n  }\n  pendingCollection {\n    id\n    __typename\n  }\n  pinnedAt\n  pinnedByCreatorAt\n  __typename\n}\n\nfragment MutePopoverOptions_creator on User {\n  id\n  __typename\n}\n\nfragment auroraHooks_publisher on Publisher {\n  __typename\n  ... on Collection {\n    isAuroraEligible\n    isAuroraVisible\n    viewerEdge {\n      id\n      isEditor\n      __typename\n    }\n    __typename\n    id\n  }\n  ... on User {\n    isAuroraVisible\n    __typename\n    id\n  }\n}\n\nfragment MutePopoverOptions_collection on Collection {\n  id\n  __typename\n}\n\nfragment ClapMutation_post on Post {\n  __typename\n  id\n  clapCount\n  ...MultiVoteCount_post\n}\n\nfragment MultiVoteCount_post on Post {\n  id\n  ...PostVotersNetwork_post\n  __typename\n}\n\nfragment PostVotersNetwork_post on Post {\n  id\n  voterCount\n  recommenders {\n    name\n    __typename\n  }\n  __typename\n}\n\nfragment NewsletterV3EmailToSubscribersMenuItem_post on Post {\n  id\n  creator {\n    id\n    newsletterV3 {\n      id\n      subscribersCount\n      __typename\n    }\n    __typename\n  }\n  isNewsletter\n  isAuthorNewsletter\n  __typename\n}\n\nfragment PostPresentationTracker_post on Post {\n  id\n  visibility\n  previewContent {\n    isFullContent\n    __typename\n  }\n  collection {\n    id\n    slug\n    __typename\n  }\n  __typename\n}\n\nfragment PostPreviewAvatar_post on Post {\n  __typename\n  id\n  collection {\n    id\n    name\n    ...CollectionAvatar_collection\n    __typename\n  }\n  creator {\n    id\n    username\n    name\n    ...UserAvatar_user\n    ...userUrl_user\n    __typename\n  }\n}\n\nfragment CollectionAvatar_collection on Collection {\n  name\n  avatar {\n    id\n    __typename\n  }\n  ...collectionUrl_collection\n  __typename\n  id\n}\n\nfragment collectionUrl_collection on Collection {\n  id\n  domain\n  slug\n  __typename\n}\n\nfragment UserAvatar_user on User {\n  __typename\n  id\n  imageId\n  mediumMemberAt\n  name\n  username\n  ...userUrl_user\n}\n\nfragment userUrl_user on User {\n  __typename\n  id\n  customDomainState {\n    live {\n      domain\n      __typename\n    }\n    __typename\n  }\n  hasSubdomain\n  username\n}\n"}
request = req.Request(url, headers = {
  "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
  "Content-Type":"application/json",
}, data=json.dumps(requestData).encode("utf-8"))
with req.urlopen(request) as response:
  data = response.read().decode("utf-8")
data = json.loads(data)
print(data["data"]["extendedFeedItems"][0]["post"]["title"] #試著印出第一篇文章的標題


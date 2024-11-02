import feedparser
import time
URL="https://wvssm.tistory.com/rss" # URL = "내블로그 주소/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

# 기본적으로 바뀌지 않을 Markdown text 입력
markdown_text = """
```bash
wvssm
├─ backend
│  ├─ Spring_Boot     
│  ├─ Java
│  └─ MySQL  
├─ etc         
│  ├─ Algorithm  
│  ├─ Blog
│  └─ Computer_Science   
└─ learning..       
   ├─ Docker
   └─ Kubernetes           

```  

## Latest Tistory Posting<div class=blog-post text-align='left'>
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']})\n"
markdown_text +=  """
</div>
</div>
"""
print(markdown_text)
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()

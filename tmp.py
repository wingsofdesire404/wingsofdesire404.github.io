import requests
from bs4 import BeautifulSoup
import urllib

# 定义要爬取的网页链接
url = 'chrome-extension://ghppfgfeoafdcaebjoglabppkfmbcjdd/explorer.html?181568198#interest'  # 替换成你要爬取的网页链接

# 发送请求获取网页内容
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到所有的图片标签
img_tags = soup.find_all('img')

# 遍历图片标签，获取图片链接并下载
for img_tag in img_tags:
    img_url = img_tag.get('src')
    # 处理相对路径的情况
    if not img_url.startswith('http'):
        img_url = urllib.parse.urljoin(url, img_url)
    
    # 下载图片
    img_data = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    with open(img_name, 'wb') as f:
        f.write(img_data)
        print(f"已下载图片: {img_name}")

print("所有图片下载完成！")

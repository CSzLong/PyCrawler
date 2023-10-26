import ssl
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

ssl._create_default_https_context = ssl._create_unverified_context
urlstr = "https://movie.douban.com/top250?start=0&filter="
headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

# response = Request(urlstr, headers=headers)
rp = requests.get(urlstr, headers=headers)
# html = urlopen(response)
# bs = bs(html.read(), 'html.parser')
bs = BeautifulSoup(rp.text, 'html.parser')
# namelist = bs.find_all('span', {'class': {'title', 'other'}})
namelist = bs.find_all(name="span", attrs={'class': {'title', 'other'}})

if __name__ == '__main__':
    for name in namelist:
        print(name.get_text().replace(" / ", '').replace("  ", ""))

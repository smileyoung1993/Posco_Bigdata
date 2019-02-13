#
import bs4

# web scraping


# web crawling

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn'
page = urlopen(url)
soup = BeautifulSoup(page, "html.parser")
result = soup.find_all("div", attrs={"class":"tit3"})

i = 1
for movie in result:
    print("%2d위" % i , end=' ')
    print(movie.get_text().strip())
    i += 1
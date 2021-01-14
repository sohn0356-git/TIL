from urllib import request
import bs4

html_website = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId-108")
soup = bs4.BeautifulSoup(html_website, "html.parser")

for city in soup.select("location"):
    name = city.select_one("city").string
    wf = city.select_one("wf").string
    tmn = city.select_one("tmn").string
    tmx = city.select_one("tmx").string
    print("%s : %s(%s~%s)" % (name, wf, tmn, tmx))
import requests
from bs4 import BeautifulSoup
import time
import json
import random
from datetime import datetime
import sqlite3


# config some proxy, for avoiding block
def get_free_proxy():
    url = "https://free-proxy-list.net/"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    proxy = []
    for row in soup.find(
        "table", attrs={"class": "table table-striped table-bordered"}
    ).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxy.append(str(ip) + ":" + str(port))
        except IndexError:
            continue

    return proxy


# proxy = get_free_proxy()


class GetNewsLink:
    def __init__(self):
        self.url = "https://sputniknews.com/"
        self.links = []

    def GetSOurceCode(self):
        # p = random.choice(proxy)
        # try:
        #     r = requests.get(self.url, proxies={"http":'45.94.45.254:7257', "https":'45.94.45.254:7257'})
        #     if r.status_code == 200:
        #         self.BeautifulSoupProcess(r.content)
        #     # return the links we got
        #     return self.links
        # except:
        #     print("bad")
        r = requests.get(self.url)
        if r.status_code == 200:
            self.BeautifulSoupProcess(r.content)
        return self.links

    def BeautifulSoupProcess(self, context):
        soup = BeautifulSoup(context, "lxml")
        self.LatestNewsLinks(soup)
        self.GetOtherLinks(soup)

    def LatestNewsLinks(self, soup):
        ## use inspection to find the link class of the data
        links = soup.find_all("a", attrs={"class": "cell-main-photo__image"})
        ## access the links one by one
        for link in links:
            ## extract the reference of those photos
            # print(link.get("href"))
            ## if we get something that we don't want, we find the difference in their structure
            if link.find_parent("div", attrs={"data-floor": 1}):
                # we extract sub-links in the parent list
                href = self.url + link.get("href")
                # the second parameter is the classification name
                self.links.append((href, "latest"))
                # print(link.get("href"))

    ## we also want some subsections news in the page
    def GetOtherLinks(self, soup):
        otherLinks = soup.find_all("a", attrs={"class": "cell-list__item"})
        for link in otherLinks:
            # at the same time we want the title of sections
            category = (
                link.find_parent(
                    "div", attrs={"class": "cell-list__list"}
                ).previous_sibling
            ).text
            href = self.url + link.get("href")
            self.links.append((href, "category"))
            # print(category)


# very pythonic way
# for link, category in linkGet:
#     print(link, category)

################################
# then we need to get the contents inside above links

# take a example of one of our links
# url = "https://sputniknews.com//20220724/celebration-galore-as-indian-javelin-star-neeraj-chopra-wins-silver-at-world-athletics-1097735843.html"


class NewsContent:
    def __init__(self, url):
        self.url = url
        # sql connection
        # ci wen jian jia under the same local file
        self.connection = sqlite3.connect("Django/sputnik_news/db.sqlite3")
        self.cursor = self.connection.cursor()
        # create a dict to store all the information we extracted
        self.detail = {}

    def GetSourceCode(self):
        # p = random.choice(proxy)
        # try:
        #     r = requests.get(self.url, proxies={"http":'45.94.45.254:7257', "https":'45.94.45.254:7257'})
        #     if r.status_code == 200:
        #         self.BeautifulSoupProcess(r.content)
        #     # return the links we got
        #     return self.links
        # except:
        #     print("bad")
        r = requests.get(self.url)
        if r.status_code == 200:
            self.BeautifulSoupProcess(r.content)
            # saved to sql
            print(self.detail)
            self.ConvertToJson(self.detail)

    def BeautifulSoupProcess(self, content):
        soup = BeautifulSoup(content, "lxml")
        self.GetDetails(soup)

    def ConvertToJson(self, dictionaryData):
        convertedData = json.dumps(dictionaryData)
        self.SaveToDatabase(convertedData)

    def SaveToDatabase(self, convertedData):
        randomNumber = random.randint(1, 1000)
        id = int(datetime.now().microsecond) + randomNumber
        # zhi xing sql insert cha ru yu ju
        self.connection.execute(
            "insert into news_newsdetail values(?,?)", [id, convertedData]
        )
        self.connection.commit()

    def GetDetails(self, soup):
        # it is best to give every extraction a try catch
        ## for each passage, we get the title
        try:
            title = soup.find("h1", attrs={"class": "article__title"}).text
        except:
            pass
        ## for each passage, we find the image
        try:
            news_image = (
                soup.find("div", attrs={"class": "media__size"}).find("img").get("src")
            )
        except:
            pass

        try:
            ## for each passage, we find the announcement
            announcement_text = soup.find(
                "div", attrs={"class": "article__announce-text"}
            ).text
        except:
            pass

        try:
            # put into the dict
            # we modify the structure of the dict that we stated in the class of new structure
            self.detail = {
                "title": title,
                "news_image": news_image,
                "announcement_text": announcement_text,
                "content": [],
            }
        except:
            pass

        ## for each passage, we find the article content
        article_body = soup.find("div", attrs={"class": "article__body"})
        # as each article consists of different subsections, we need to get all sub sections, and merge them together
        for detail in article_body:
            # if one page don't have this, we try catch the error
            try:
                journal = detail.find("div", attrs={"class": "article__text"}).text
                self.detail["content"].append({"journal": journal})

            except:
                pass

            # for other part, do the same
            try:
                quote = detail.find("div", attrs={"class": "article__quote-text"}).text
                self.detail["content"].append({"quote": quote})
            except:
                pass

            try:
                related_link = detail.find(
                    "div", attrs={"class": "article__article"}
                ).find("a")
                related_link_href = related_link.get("href")
                related_link_title = related_link.get("title")
                related_link_image = related_link.find("img").get("src")
                self.detail["content"].append(
                    {
                        "related_link": [
                            {
                                "related_link_href": related_link_href,
                                "related_link_title": related_link_title,
                                "related_link_image": related_link_image,
                            }
                        ]
                    }
                )
            except:
                pass


linkGet = GetNewsLink().GetSOurceCode()
print(linkGet)
for url, category in linkGet:
    print(url)
    NewsContent(url).GetSourceCode()
    time.sleep(1)


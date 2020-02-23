import os
import time
import json
import webbrowser
import requests
from lxml import etree
from CreatePage import CreatePage as Page


class DSpider(object):
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
                                      "(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        self.html = self.get_html()
        self.folder = time.strftime("%Y%m%d%H%M%S", time.localtime())

    def get_html(self):
        response = requests.get("https://book.douban.com", headers=self.headers)
        html_str = response.content.decode()
        html = etree.HTML(html_str)
        return html

    def spider(self):
        try:
            os.mkdir(self.folder)
        except FileExistsError:
            pass
        os.chdir(self.folder)
        Page.open(self.folder)
        li_list = self.html.xpath("//div[@class='carousel']//li")
        for li in li_list:
            self.save_book(li)
        Page.close()

    def save_book(self, li):
        info = {
            "img": li.xpath(".//img/@src")[0],
            "title": li.xpath(".//h4/text()")[0].strip(),
            "author": li.xpath(".//span[@class='author']/text()")[0].strip(),
            "year": li.xpath(".//span[@class='year']/text()")[0].strip(),
            "publisher": li.xpath(".//span[@class='publisher']/text()")[0].strip(),
            "resume": li.xpath(".//p[@class='abstract']/text()")[0].strip(),
            "link": li.xpath(".//div[@class='title']/a/@href")[0].strip()
        }
        folder = self.create_folder(info["title"])
        img = self.save_img(info["img"], folder)
        with open("%s/info.json" % folder, "w", encoding="utf-8") as file:
            file.write(json.dumps(info, ensure_ascii=False))
        Page.write(img, **info)
        print("save %s" % folder)

    def create_folder(self, folder):
        try:
            os.mkdir(folder)
        except FileExistsError:
            pass
        except NotADirectoryError:
            new_folder = folder
            error = "/\\:*?\"<>|"
            for char in new_folder:
                if char in error:
                    new_folder = new_folder.replace(char, "_")
            print("'%s' not a directory, rename '%s'" % (folder, new_folder))
            return self.create_folder(new_folder)
        return folder

    def save_img(self, url, folder):
        file = "%s/%s" % (folder, url.split("/")[-1])
        with open(file, mode="wb") as image:
            response = requests.get(url, headers=self.headers)
            image.write(response.content)
        return file

    def show_web(self):
        print("html file in '%s'" % os.getcwd())
        print("do you want to open the easy web? [y or n]: ", end="")
        if input() == "y":
            webbrowser.open("%s.html" % self.folder)


if __name__ == '__main__':
    books_express = DSpider()
    books_express.spider()
    books_express.show_web()

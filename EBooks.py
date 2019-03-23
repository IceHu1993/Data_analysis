import requests
from lxml import etree
import json
class BookSpider(object):
    def __init__(self):
        self.base_url = 'http://www.allitebooks.com/page/{}'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.data_list = []
    #构建所有的URL的方法
    def get_url_list(self):
        url_list = []
        for i in range(1,11):
            url = self.base_url.format(i)
            url_list.append(url)
        return url_list

    #发请求的方法
    def send_request(self, url):
        data = requests.get(url, headers=self.headers).content.decode()
        return data

    #解析数据
    def parse_xpath_data(self,data):
        parse_data = etree.HTML(data)
        #1.解析出所有的书 book
        book_list = parse_data.xpath('//article')
        print(len(book_list))
        #2.解析出每本书的信息
            #1.书名
        for book in book_list:
            book_dict ={}
            book_dict['book_name'] = book.xpath('//h2[@class="entry-title"]//text()')[0]
            #print(book_name)

            #2.书的图片url
            book_dict['image_url'] = book.xpath('div[@class="entry-thumbnail hover-thumb"]/a/img/@src')[0]
            #3.书的作者
            book_dict['book_author'] =book.xpath('.//h5[@class="entry-author"]//text()')
            #4.书的简介
            book_dict['book_info'] = book.xpath('.//div[@class="entry-summary"]/p/text()')[0]
            self.data_list.append(book_dict)

    #保存数据
    def save_data(self):
        json.dump(self.data_list,open("books.json","w"))

    #统筹调用
    def start(self):
        url_list = self.get_url_list()
        #循环遍历发送请求
        for url in url_list:
            data = self.send_request(url)
            self.parse_xpath_data(data)
            self.save_data()

BookSpider().start()

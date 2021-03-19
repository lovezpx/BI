import requests
from requests_html import HTMLSession

class BaiDuImg:
    session = HTMLSession()
    img_url_regex = '"thumbURL":"{}",'
    url = ''
    img_url_list = []

    def get_search(self):
        search = input()
        self.url = f'http://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word={search}'

    def get_img_url_list(self):
        response = self.session.get(self.url)
        self.img_url_list = response.html.search_all(self.img_url_regex)

    def save_img(self):
        mun = 0
        for url in self.img_url_list:
            mun += 1
            # 访问图片链接
            response = self.session.get(url[0])
            # 保存二进制并保存至本地
            with open(f'第{mun}张.jpg', 'wb') as fw:
                fw.write(response.content)

    def run(self):
        self.get_search()
        self.get_img_url_list()
        self.save_img()


if __name__ == '__main__':
    baidu = BaiDuImg()
    baidu.run()
import re
import urllib.request

class EbookCrawler:
    title = ""
    web_url = ""
    save_path = ""

    def __init__(self, title, web_url, save_path):
        self.title = title
        self.web_url = web_url
        self.save_path = save_path

    def get_html(self):
        f = open('{}.txt'.format(self.save_path + self.title), 'a+')

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }
        # 生成一个请求报文，这里的url和data需要提前给定
        req = urllib.request.Request(self.web_url, headers=headers)
        # 获取网页源代码
        html = urllib.request.urlopen(req).read()
        # 转成该网站格式
        html = html.decode("gbk")

        # 根据网站样式匹配的正则：(.*?)可以匹配所有东西，加括号为我们需要的
        reg = r'<dd><a href ="(.*?)">(.*?)</a></dd>'
        reg = re.compile(reg)
        urls = re.findall(reg, html)

        for url in urls:

            print(url)
            chapter_url = "https://www.biqumo.com" + url[0] #章节路径
            chapter_title = url[1] #章节名
            chapter_html = urllib.request.urlopen(chapter_url).read() #获取该章节的全文代码
            chapter_html = chapter_html.decode("gbk")
            # 匹配文章内容
            chapter_reg = r'<div id="content" class="showtxt"><script>.*?</script>(.*?)<script>.*?</script>.*?<script>.*?</script>.*?</div>'
            chapter_reg = re.compile(chapter_reg,re.S)
            chapter_content = re.findall(chapter_reg, chapter_html)
            for content in chapter_content:
                # 使用空格代替
                content = content.replace("&nbsp;&nbsp;&nbsp;&nbsp;", "")
                # 使用空格代替
                content = content.replace("<br />", "")
                # 保存到本地
                f.write(chapter_title)
                f.write("\n\n")
                f.write(content)
                f.write("\n\n")

        f.close()


if __name__ == '__main__':
    downloadTxt = EbookCrawler(title="庆余年", web_url="https://www.biqumo.com/8_8521/",
                               save_path="C:/Users/lovezpx/Desktop/")
    downloadTxt.get_html()
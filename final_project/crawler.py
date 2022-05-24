import requests
from lxml import etree
import json

headers = {
    # 此处的cookie为翻页时候提取的cookie
    "Cookie": "wdcid=2c1008ae99960cdf; UM_distinctid=17cdb56878c89c-0200b6372d3363-a7d173c-186a00-17cdb56878d9b7; __asc=f667c92517cdb5688ae3ad4667f; __auc=f667c92517cdb5688ae3ad4667f",
    "Host": "https://olympics.com/",
    "Referer": "https://olympics.com/zh/olympic-games/beijing-2022/results",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
    "X-Requested-With": "XMLHttpRequest"
}

def get_resp(url):
    response = requests.get(headers=headers, url=url)
    return response

def save_data(url, title, category, content, f):
    data_dic = {}
    data_dic["url"] = url
    data_dic["title"] = title
    data_dic["category"] = category
    data_dic["content"] = content
    f.write(json.dumps(data_dic, ensure_ascii=False) + '\n')

def get_url_per_detail(response, url, f):
    e = etree.HTML(response.text)

    title_list = e.xpath('//div[@class="title_thema"]//text()')
    category_list = e.xpath('//div[@class="wrap hd_map"]//text()')
    content_list = e.xpath('//div[@class="content_topp"]//text()')

    title = "".join(title_list)
    category = "".join(category_list)
    content = "".join(content_list)

    # print(title)
    # print(category)
    # print(content)
    # print(url)
    save_data(url, title, category, content, f=f)

if __name__ == '__main__':
        # i = 1
        # for page in range(150):
        #     print(f"、、、、、、、、当前正在爬取第{i}个词汇、、、、、、、、")
        #     url = f"http://www.jinrongbaike.com/doc-view-{7554 + page}.htm"
        #
        #     resp = get_resp(url=url)
        #     print(resp)
        #     if resp.status_code == 200:
        #         # 处理每一页具体内容
        #         with open(f"crawler_data/{page}.json", mode="wt", encoding="utf-8") as f:
        #             get_url_per_detail(response=resp, url=url, f=f)
        #
        #     i += 1

        url = f"http://www.jinrongbaike.com/doc-view-7554.htm"
        resp = get_resp(url=url)
        print(resp,resp.text)
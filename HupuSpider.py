# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request as r

import utils


def download(url):
    print('        Downloading ' + url)

    if url is None:
        return None

    request = r.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36')

    response = r.urlopen(request)

    return response.read()


def parse(url, html_content):
    print('        Parsing ' + url)

    if url is None or html_content is None:
        return None

    soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
    new_data = get_new_data(soup)

    return new_data


def get_new_data(soup):
    res_data = []

    title_nodes = soup.find_all("div", {"class": "titlelink box"})

    for node in title_nodes:
        text = node.get_text()
        trimmed_text = utils.trim_text(text, True, True)
        res_data.append(trimmed_text)

    return res_data


def crawl(url):
    print('    Crawling ' + url)
    html_content = download(url)
    new_data = parse(url, html_content)
    return new_data

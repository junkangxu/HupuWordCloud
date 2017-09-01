# -*- coding: utf-8 -*-
import sys

import HupuSpider
import HupuWordSplit
import HupuCounter
import HupuWordCloud
import utils

reload(sys)
sys.setdefaultencoding("utf-8")

# BASE_URL = "https://bbs.hupu.com/lakers"
BASE_URL = "https://bbs.hupu.com/"
DIVISIONS = ["vote", "nba", "10w",
             "rockets", "cavaliers", "warriors", "lakers", "spurs", "celtics",
             "thunder", "clippers", "knicks", "bulls", "timberwolves", "mavericks",
             "nets", "sixers", "pacers", "blazers", "heat", "wizards",
             "jazz", "grizzlies", "suns", "kings", "pelicans", "bucks",
             "raptors", "nuggets", "hawks", "pistons", "magic", "hornets"]


def crawler(div):
    template_url = BASE_URL + div
    print "2. Start to crawl on " + template_url

    urls = utils.generate_urls(template_url)

    filename = './' + div + '/titles.txt'

    f = open(filename, 'w')
    for url in urls:
        titles = HupuSpider.crawl(url)

        for title in titles:
            f.write(title + '\n')

    f.close()

    print '--------------------------'


def segment(div):
    print "3. Start to segment " + div + " titles"
    HupuWordSplit.segment_titles(div)
    print '--------------------------'


def count(div):
    print "4. Start to count frequency " + div + " keywords"
    HupuCounter.calculate_frequency(div)
    print '--------------------------'


def create(div):
    print "5. Start to create Word Cloud " + div
    HupuWordCloud.create_word_cloud(div)
    print '--------------------------'


def get_user_input():
    print "1. Get user input:"
    while True:
        user_input = raw_input("    Choose a division: ")
        lowered_user_input = user_input.lower()
        if lowered_user_input in DIVISIONS:
            print '--------------------------'
            return lowered_user_input
        else:
            print "    Your input is not a valid division"


if __name__ == "__main__":
    print "Welcome to Hupu Word Cloud"
    print "=========================="

    division = get_user_input()

    crawler(division)

    segment(division)

    count(division)

    create(division)

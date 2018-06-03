# coding:utf-8
import jieba
import sys
from imp import reload

reload(sys)
jieba.load_userdict("./user_dict.txt")


def segment_titles(div):
    input_file = open('./titles/' + div + '.txt', "r")
    output_file = open("./segmented_titles/" + div + ".txt", "w")

    lines = input_file.readlines()

    for line in lines:
        segmented_line = jieba.cut_for_search(line)
        output_file.write('\n'.join(segmented_line))

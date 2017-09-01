# encoding=utf-8
from collections import OrderedDict

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def calculate_frequency(div):
    input_file = open("./" + div + "/segmented_titles.txt", "r")
    output_file = open("./" + div + "/calculated_titles.txt", "w")

    lines = input_file.readlines()

    word_map = {}

    for line in lines:
        if line not in word_map:
            word_map[line] = 1
        else:
            word_map[line] += 1

    sorted_word_map = OrderedDict(sorted(word_map.items(), key=lambda x: x[1], reverse=True))

    for (k, v) in sorted_word_map.items():
        output_file.write("%s: %s" % ((k.replace('\n', '')).encode('utf-8'), str(v) + '\n'))

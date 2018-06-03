# encoding=utf-8
from collections import OrderedDict

import sys
from imp import reload

reload(sys)


def calculate_frequency(div):
    input_file = open("./segmented_titles/" + div + '.txt', "r")
    output_file = open("./calculated_titles/" + div + ".txt", "w")

    lines = input_file.readlines()
    word_map = {}

    for line in lines:
        if line not in word_map:
            word_map[line] = 1
        else:
            word_map[line] += 1

    sorted_word_map = OrderedDict(sorted(word_map.items(), key=lambda x: x[1], reverse=True))

    for (k, v) in sorted_word_map.items():
        output_file.write("%s: %s" % ((k.replace('\n', '')), str(v) + '\n'))

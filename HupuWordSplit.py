import jieba

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
jieba.load_userdict("./user_dict.txt")


def segment_titles(div):
    input_file = open('./' + div + '/titles.txt', "r")
    output_file = open("./" + div + "/segmented_titles.txt", "w")

    lines = input_file.readlines()

    for line in lines:
        segmented_line = jieba.cut_for_search(line)
        output_file.write('\n'.join(segmented_line))

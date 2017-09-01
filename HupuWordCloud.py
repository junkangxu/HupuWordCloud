# encoding=utf-8
import matplotlib.pyplot as plt

import wordcloud
import jieba


def create_word_cloud(div):
    text = open('./' + div + '/calculated_titles.txt').read()
    text_after_cut = jieba.cut(text, cut_all=False)
    text_after_joined = " ".join(text_after_cut)

    background_image = plt.imread('./images/' + div + '.jpg')
    word_cloud = wordcloud.WordCloud(background_color='white',
                                     mask=background_image,
                                     font_path="/System/Library/Fonts/Hiragino Sans GB W3.ttc")\
        .generate(text_after_joined)

    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

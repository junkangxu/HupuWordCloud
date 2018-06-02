# encoding=utf-8
import matplotlib.pyplot as plt

import wordcloud
import jieba

# read common chinese stopwords from file
def get_stopwords():
    text = open('./stopwords.txt', 'r')
    stopwords = set()
    for line in text:
        stopwords.add(line)
    return stopwords

# create wordcloud
def create_word_cloud(div):
    text = open("./calculated_titles/" + div + ".txt", "r").read()
    text_after_cut = jieba.cut(text, cut_all=False)
    text_after_joined = " ".join(text_after_cut)

    word_cloud = wordcloud.WordCloud(background_color='white',
                                     stopwords=get_stopwords(),
                                     font_path="/System/Library/Fonts/Hiragino Sans GB W3.otf")\
        .generate(text_after_joined)

    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

    word_cloud.to_file("./images/" + div + '.jpg')

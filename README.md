# HupuWordCloud
Create Word Cloud from different subdirectory of **https://bbs.hupu.com/**

## Purpose
Create Word Cloud based on most frequent words in different subdirectory of **hupu**

## Workflow
- scrape top 100 pages of most recently replied posts with **urllib** (updated 06/02/2018)
- Use **jieba** to segment Chinese phrases
- Use **WordCloud** to generate matplotlib graph based on the frequency of key words (excluded common chinese stopwords)

## Update
- Sept 1st, 2017
  - I tested it for **lakers** subdirectory, so I only added Lakers' logo into *images* folder.
  - Added a little bit of words into user dictionary in **user_dict.txt**. And will add more when testing all the other subdirectories.
  - Haven't specified **stopwords**
- Jun, 2nd, 2018
  - works for **vote** subdirectory
  - remove background images because some teams have too much white backgrounds on their logos
  - Added common **stopwords** as *stopwords.txt*
  - migrated from Python 2.7 to Python 3.5

## Requirements
- **Python 3.5**
- **urllib** (preinstalled standard package for Python 3.5)
- **jieba** (package used to parse Chinese phrases)
- **WordCloud** (package used to generate WordCloud)
- **Hiragino Sans GB W3.otf** (It's required for displaying Chinese words, you can change it to any Chinese fonts by changing the parameter *font* of *WordCloud*)

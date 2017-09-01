# HupuWordCloud
Create Word Cloud from different subdirectory of **https://bbs.hupu.com/**

## Purpose
Create Word Cloud based on most frequent words in different subdirectory of **hupu**

## Workflow
- Crawl top 100 pages of the bbs with **urllib2** (updated 9/1/2017)
- Use **jieba** to segment Chinese phrases
- Use **WordCloud** to generate matplotlib graph based on the frequency of key words appear in the title of different posts

## Update
- Sept 1st, 2017
  - I tested it for **lakers** subdirectory, so I only added Lakers' logo into *images* folder.
  - Added a little bit of words into user dictionary in **user_dict.txt**. And will add more when testing all the other subdirectories.
  - Haven't specified **stopwords**

## Requirements
- **Python 2.7**
- **urllib2** (preinstalled standard package for Python 2.7)
- **jieba** (package used to parse Chinese phrases)
- **WordCloud** (package used to generate WordCloud)

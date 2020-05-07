# 本应用的前缀是word, 主要用来解决词语方面的分析


### 结构

├── db.sqlite3
├── manage.py
├── mysite
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── word                                   --word app
    ├── admin.py
    ├── apps.py
    ├── dataPro.py                         --数据处理函数, 主要数据处理在里面
    ├── __init__.py
    ├── migrations
    │   ├── __init__.py
    │   └── __pycache__
    │       └── __init__.cpython-38.pyc
    ├── models.py
    ├── __pycache__
    │   ├── admin.cpython-38.pyc
    │   ├── __init__.cpython-38.pyc
    │   ├── models.cpython-38.pyc
    │   ├── urls.cpython-38.pyc
    │   └── views.cpython-38.pyc
    ├── README.md
    ├── tests.py
    ├── urls.py                            --url设置
    └── views.py                           --试图函数



## 关于本项目的NLP处理目标规划
- 长文本相似度匹配
个人水平有限,感觉官方数据不适合有监督学习的办法,(询问相关人员后也觉得只能是无间督)
对于官方数据,我只有两种思路
1, 用无间督学习的办法,
2,用迁移学习,但是网上好像没有很好的迁移学习提取语义向量的模型,(可能只是我没找到吧)

- 句子主谓宾分析,识别否定词
使用pyhanlp进行句子分词,语法依存分析.

- 动词,形容词,副词,等,与原词的相似性匹配

- 常见名词及其解释的匹配
直接调用百度接口更好,用爬虫解决.

- 题目按点给分
先提取出语义实体,那么下一部就做提取语义实体


- 主动判分


## 目前计划任务
一步一步走,不能急功近利.
无论怎样,自己现在确实缺少能力去完成.
所以,将问题分解,只求做完部分就行.

nlp不是简单的lstm.nlp是自然语言处理.
从头开始,一点点系统的进行学习nlp问题的处理.


任务:
- 首先,句子分析问题吧.
依存分析和句子相似度可以调用相关NLP库解决,不过对于数据预处理方面要多加注意.

- 对于实体提取


同时:
- 用django做一个简单的demo吧.
我只返回一下接口
- 返回句子样例列表.
- 各种词性分析数据,主谓宾
- 词语相似度匹配.


## 工具简介:
pyhanlp:

中文分词
词性标注
命名实体识别
依存句法分析
关键词提取新词发现
短语提取
自动摘要
文本分类


## 关于模型原理
- 命名体识别的算法，其实主要的方法就是HMM和CRF了，因为可以转换为标注问题，这里都可以使用HMM和CRF，
同时大多数的词法分析原理也是这俩,(也不全算,但是常用)
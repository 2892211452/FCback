import requests
import pandas as pd
import numpy as np
from pyhanlp import *
from gensim.models import word2vec
import os
# -*- coding: utf-8 -*-
import re
import pandas as pd
import numpy as np
from pyhanlp import *


filePath =  os.path.dirname(os.path.abspath(__file__))

#解释词语
def explainWord( word="人"):
    url = "https://www.zdic.net/hans/"+ word


    headers = {
        'cache-control': "no-cache",
        'postman-token': "702711ea-ebc8-ba16-337f-a30fed90b0ba"
        }

    response = requests.request("GET", url, headers=headers)

    html = response.text
    import re
    from bs4 import BeautifulSoup as bs
    soup = bs(html, 'html5lib')

    video = soup.find(attrs={'class':'audio_play_button i_volume-up ptr'})
    video = video.get('data-src-mp3')


    #找释义 父节点
    ex = soup.find('ol').text
    ans ={'video':video, 'ex':ex}


    return ans


#语法依存 主谓宾
def grammer(sentence="徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"):
    #进行语法依存分析
    sentence = HanLP.parseDependency(sentence)
    ans = []
    for word in sentence.iterator():  # 通过dir()可以查看sentence的方法
        ans.append([word.LEMMA, word.DEPREL, word.HEAD.LEMMA])
    return ans




#计算两个词语相似度
def WordSim(word1, word2):
    sentences = word2vec.Text8Corpus(filePath +"/text.txt")# 加载语料
    n_dim = 200
    model = word2vec.Word2Vec(sentences, size=n_dim, min_count=5,sg=1)
    return model.similarity(word1,word2)





#计算语句的向量
def getVecter(s1, s2):
    from gensim.models import word2vec

    sentences = word2vec.Text8Corpus("/home/lwl/code/jupyter/NLP服创/text.txt")# 加载语料
    n_dim = 200
    model = word2vec.Word2Vec(sentences, size=n_dim, min_count=5,sg=1)

    x = model['仓库']    

    word_vector1 = np.zeros(len(x))
    word_vector2 = np.zeros(len(x))


    terms = HanLP.segment(s1)  
    for term in terms:
            x = model[term.word]
            word_vector1 = word_vector1 + x



    terms = HanLP.segment(s2)  
    for term in terms:
            x = model[term.word]
            word_vector2 = word_vector2 + x

    return word_vector1, word_vector2



#计算余弦
def cos_dist(vec1,vec2):
    """
    :param vec1: 向量1
    :param vec2: 向量2
    :return: 返回两个向量的余弦相似度
    """
    dist1=float(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
    return dist1


#计算语句的相似度
def getSenSim(s1, s2):
    vec1,vec2=getVecter(s1,s2)
    dist1=cos_dist(vec1,vec2)
    return dist1


if __name__ == '__main__':
    s1="仓储是指利用仓库及相关设施设备进行物品的入库"
    s2="仓储是指利用仓库及相关设施设备进行物品的入库。"
    ans = getSenSim(s1, s2)
    print(ans)






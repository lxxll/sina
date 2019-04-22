# -*- coding:utf-8 -*-
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


filename = "content.txt"
with open(filename,encoding='utf-8') as f:
    mytext = f.read()



f=open("Stopword.txt",encoding='utf-8')
stopwords={}.fromkeys(f.read().split("\n"))
f.close()



segs=jieba.cut(mytext)

mytext_list=[]
#文本清洗
for seg in segs:
    if seg not in stopwords and seg!=" " and len(seg)!=1:
        mytext_list.append(seg.replace(" ",""))
cloud_text=",".join(mytext_list)


wordcloud = WordCloud(font_path="simsun.ttf",max_words=200, background_color="white",min_font_size=15,max_font_size=80, width=400).generate(cloud_text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

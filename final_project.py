#encoding:utf-8
"""
要求使用python编写程序，实现对《黎明破晓的街道》文本中人物关系的提取，并利用Gelphi软件对人物关系可视化，生成如下类似人物关系图谱。
作者：赖垚旭
"""

import os,sys
import jieba,codecs,math
import jieba.posseg as pseg


names={}  #姓名字典
relationships={} #关系字典
lineNames=[]  #每段人物关系
jieba.load_userdict('zidian.txt')#设置字典,加载


with codecs.open("黎明破晓的街道.txt",'r','gbk') as f:
	for line in f.readlines():
		poss=pseg.cut(line)
		lineNames.append([])
		for w in poss:   #nr词频，
			if  w.flag!="nr" or len(w.word) <2:
				continue
			lineNames[-1].append(w.word)
			if names.get(w.word) is None:
				names[w.word]=0
				relationships[w.word]={}
			names[w.word]+=1
	for name,times in names.items():
		print (name,times)



#根据识别结果构架网络
for line in lineNames:  #对于每一段
	for name1 in line:
		for name2 in line: #每一段中两个任意人
			if name1==name2:
				continue
		if relationships[name1].get(name2) is None:
			relationships[name1][name2]=1
		else:
			relationships[name1][name2]+=1



#过滤冗余的边并输出结果，将已经建立好的names和relationships输出到文本
#节点集合保存在busan_node.txt
#边集合保存在busan_edge.node
with codecs.open('黎明破晓的街道节点.csv','w','gbk') as f:
	f.write("id lable weight\r\n")
	for name,times in names.items():
		f.write(name+" "+name+" "+str(times)+"\r\n")
with codecs.open('黎明破晓的街道边.csv','w','gbk') as f:
	f.write("source target weight\r\n")
	for name,edges in relationships.items():
		for v, w in edges.items():
			if w>3:
				f.write(name+ " "+v+" "+str(w)+"\r\n")

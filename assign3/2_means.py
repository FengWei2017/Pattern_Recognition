#*********************************************************
# Programmer : Feng Wei
# Date: April 7 2017
# Course: ECE8560 Pattern Recognition
# Clemson University School of Computing
# classification program
# Use c_means to classify the test data
#**********************************************************
from numpy import *
import math
from sklearn.cluster import KMeans
# Read train data test data, and open a file to write result
write = open("wei8-classified-2means.txt", "a")
train = open("train_sp2017_v19", "r")
trainlines = train.readlines()
trainlst = []
for line in trainlines:
    word = line.split()
    trainlst.append(word)
# train svm
print len(trainlst)
kmeans = KMeans(n_clusters=2, random_state=0).fit(trainlst)
p = kmeans.labels_
print kmeans.cluster_centers_
c1 = 0
c2 = 0
for c in p:
    if c == 0:
	c1 += 1
        write.write("1\n")
    else:
	c2 += 1
	write.write("2\n")
print c1
print c2

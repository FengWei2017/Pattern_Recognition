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
write = open("wei8-classified-5means.txt", "a")
train = open("train_sp2017_v19", "r")
trainlines = train.readlines()
trainlst = []
for line in trainlines:
    word = line.split()
    trainlst.append(word)
# train svm
print len(trainlst)
kmeans = KMeans(n_clusters=5, random_state=0).fit(trainlst)
p = kmeans.labels_
print kmeans.cluster_centers_
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
for c in p:
    if c == 0:
	c1 += 1
        write.write("1\n")
    elif c == 1:
	c2 += 1
        write.write("2\n")
    elif c == 2:
	c3 += 1
	write.write("3\n")
    elif c == 3:
        c4 += 1
        write.write("4\n")
    else:
        c5 += 1
        write.write("5\n")

print c1
print c2
print c3
print c4
print c5

# *********************************************************
# Programmer : Feng Wei
# Date: March 7 2017
# Course: ECE8560 Pattern Recognition
# Clemson University School of Computing
# classification program
# Use knn to classify the test data
# **********************************************************
from numpy import *
import math
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(
    n_neighbors=5, weights='uniform', algorithm='kd_tree')
# Read train data test data, and open a file to write result
write = open("wei8-classified-5nn.txt", "a")
train = open("train_sp2017_v19", "r")
test = open("test_sp2017_v19", "r")
trainlines = train.readlines()
testlines = test.readlines()
trainlst = []
testlst = []
lable = []
i = 0
for line in testlines:
    word = line.split()
    testlst.append(word)
testarray = asarray(test)
for line in trainlines:
    i += 1
    word = line.split()
    trainlst.append(word)
    if i <= 5000:
        lable.append(1)
    elif i <= 10000:
        lable.append(2)
    else:
        lable.append(3)
for sample in testlst:
    tsample = asarray(sample)
    neigh.fit(trainlst, lable)
    c = neigh.predict(tsample.reshape(1, -1))
    # trainlst.append(sample)
    if c == 1:
        write.write("1\n")
        # lable.append(1)
    elif c == 2:
        write.write("2\n")
        # lable.append(2)
    else:
        write.write("3\n")
        # lable.append(3)

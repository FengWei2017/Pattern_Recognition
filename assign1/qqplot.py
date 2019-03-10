#*********************************************************
# Programmer : Feng Wei
# Date: February 7 2017
# Course: ECE8560 Pattern Recognition
# Clemson University School of Computing
# plot program
# plot hist and q-q plot
#**********************************************************

import scipy.stats as stats
from matplotlib import pyplot as plt
from numpy import *
# open and read train data
train = open("train_sp2017_v19", "r")
trainlines = train.readlines()
alst = []
blst = []
clst = []
i = 0
for line in trainlines:
    i += 1
    word = line.split()
    if i <= 5000:
        alst.append(word)
    elif i <= 10000:
        blst.append(word)
    else:
        clst.append(word)
aarray = asarray(alst)
taarray = transpose(aarray)
barray = asarray(blst)
tbarray = transpose(barray)
carray = asarray(clst)
tcarray = transpose(carray)
# plot histgram and qqplot for each dimension of 3 classes
ta = [taarray, tbarray, tcarray]
flag = 0
for ty in ta:
    for flag in range(0, 3):
        column = ty[[flag], :]
        ac = column.astype(float)
        ad = transpose(ac)
        aa = mean(ad)
        sd = std(ad)
        plt.figure(1)
        bins = arange(aa-3*sd, aa+3*sd, 0.1)
        plt.hist(ad, bins=bins, alpha=0.5)
        plt.title("Hist")
        plt.xlabel('X')
        plt.ylabel('Value')
        plt.figure(2)
        ae = hstack(ad)
        stats.probplot(ae, dist="norm", plot=plt)
        plt.show()

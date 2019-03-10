#*********************************************************
# Programmer : Feng Wei
# Date: April 7 2017
# Course: ECE8560 Pattern Recognition
# Clemson University School of Computing
# classification program 
# Use svm to classify the test data
#**********************************************************
from numpy import *
import math
from sklearn import svm
rbf_svc = svm.SVC(kernel='rbf',gamma=0.001)
# Read train data test data, and open a file to write result
write=open("wei8-classified-rbf_svm.txt","a")
train=open("train_sp2017_v19","r")
test=open("test_sp2017_v19","r")
trainlines= train.readlines()
testlines=test.readlines()
trainlst=[]
testlst=[]
lable=[]
j=0 
i=0
for line in testlines:
    if j==0:
	j+=1
    elif j==1:
	j+=1 
        word=line.split()
        testlst.append(word)
    else:
	j=0
	word=line.split()
	testlst.append(word)
for line in trainlines:
    i+=1
    word=line.split()
    if i<=5000:
        lable.append(0)
	trainlst.append(word)
    elif i<=10000:
        lable.append(1)
	trainlst.append(word)
# train svm
print len(trainlst)
print len(testlst)
rbf_svc.fit(trainlst,lable)
p=rbf_svc.predict(testlst)
for c in p: 
    if c==0:
        write.write("1\n")
    else:
        write.write("2\n")
print rbf_svc.n_support_
print rbf_svc.dual_coef_
print rbf_svc.intercept_


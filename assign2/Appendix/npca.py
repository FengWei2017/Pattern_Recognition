#*********************************************************
# Programmer : Feng Wei
# Date: March 7 2017
# Course: ECE8560 Pattern Recognition
# Clemson University School of Computing
# classification program 
# First define the Probability Density Function
# Second PCA
# Then compute the mean and sigma of each features for 3 class
# Finaly use this model to classify the test data
#**********************************************************
from numpy import *
import math
from matplotlib.mlab import PCA
from sklearn import preprocessing
#********************************************
m1=[ 50.11712203,  -4.97038793, -24.81182102, -49.81198585]
m2=[ 24.13111767,  -0.11837553, -25.04828746, 0.29147143]
m3=[ 49.70218541,   5.40154144,  24.55009373, -49.93734216]
cov1=[236.19594156,   218.99825698,  224.41664637, 648.65405355]
cov2=[2454.81250858, 626.82721073,  25.58215206,  1610.92476989]
cov3=[642.9312398, 2486.55244034,   628.68551414,    24.57683837]
# Define Probability Density Function
def norm_pdf_multivariate(x, mu, sigma):
    size = len(x)
    if size == len(mu) and (size, size) == sigma.shape:
        det = linalg.det(sigma)
        if det == 0:
            print "error"
        norm_const = 1.0/ ( math.pow((2*pi),float(size)/2) * math.pow(det,1.0/2) )
        x_mu =matrix(x - mu)
        inv = sigma.I
        result = math.pow(math.e, -0.5 * (x_mu * inv * x_mu.T))
        return norm_const * result
    else:
        print "error"
# Read train data test data, and open a file to write result
write=open("wei8-classified-npca.txt","a")
train=open("train_sp2017_v19","r")
test=open("test_sp2017_v19","r")
trainlines= train.readlines()
testlines=test.readlines()
alst=[]
blst=[]
clst=[]
testlst=[]
i=0
for line in testlines:
    word=line.split()
    testlst.append(word)
testarray=asarray(test)
for line in trainlines:
    i+=1
    word=line.split()
    if i<=5000:
	nword=subtract(asarray(word).astype(float),asarray(m1))
	mword=[0,0,0,0]
        mword[0]=nword[0]/math.sqrt(cov1[0])
        mword[1]=nword[1]/math.sqrt(cov1[1])
        mword[2]=nword[2]/math.sqrt(cov1[2])
        mword[3]=nword[3]/math.sqrt(cov1[3])
        alst.append(mword)
    elif i<=10000:
	nword=subtract(asarray(word).astype(float),asarray(m2))
	mword=[0,0,0,0]
        mword[0]=nword[0]/math.sqrt(cov2[0])
        mword[1]=nword[1]/math.sqrt(cov2[1])
	mword[2]=nword[2]/math.sqrt(cov2[2])
	mword[3]=nword[3]/math.sqrt(cov2[3])
        blst.append(mword)
    else:
	nword=subtract(asarray(word).astype(float),asarray(m3))
	mword=[0,0,0,0]
        mword[0]=nword[0]/math.sqrt(cov3[0])
        mword[1]=nword[1]/math.sqrt(cov3[1])
        mword[2]=nword[2]/math.sqrt(cov3[2])
        mword[3]=nword[3]/math.sqrt(cov3[3])
        clst.append(mword)
#PCA determinie first feature and second feature
aarray=asarray(alst)
barray=asarray(blst)
carray=asarray(clst)
aresults = PCA(aarray.astype(float))
print aresults.fracs
bresults = PCA(barray.astype(float))
print bresults.fracs
cresults = PCA(carray.astype(float))
print cresults.fracs
# Compute mean and sigma(covariance matrix)
afeature=dot(aarray.astype(float),aresults.Wt[:,[0,1]])
afeaturef=afeature.astype(float)
amean=mean(afeaturef,0)
acov=cov(afeaturef.T)
bfeature=dot(barray.astype(float),bresults.Wt[:,[0,1]])
bfeaturef=bfeature.astype(float)
bmean=mean(bfeaturef,0)
bcov=cov(bfeaturef.T)
cfeature=dot(carray.astype(float),cresults.Wt[:,[0,1]])
cfeaturef=cfeature.astype(float)
cmean=mean(cfeaturef,0)
ccov=cov(cfeaturef.T)
#Uncorrelated Components 
acov=diag(acov.diagonal())
bcov=diag(bcov.diagonal())
ccov=diag(ccov.diagonal())
print acov
print bcov
print ccov
#classify test data
c1=0
c2=0
c3=0
for sample in testlst:
    tsample=transpose(asarray(sample))
    fsample=tsample.astype(float)
    nword=subtract(fsample,transpose(asarray(m1)))
    fasample=[0,0,0,0]
    fasample[0]=nword[0]/math.sqrt(cov1[0])
    fasample[1]=nword[1]/math.sqrt(cov1[1])
    fasample[2]=nword[2]/math.sqrt(cov1[2])
    fasample[3]=nword[3]/math.sqrt(cov1[3])
    nword=subtract(fsample,transpose(asarray(m2)))
    fbsample=[0,0,0,0]
    fbsample[0]=nword[0]/math.sqrt(cov2[0])
    fbsample[1]=nword[1]/math.sqrt(cov2[1])
    fbsample[2]=nword[2]/math.sqrt(cov2[2])
    fbsample[3]=nword[3]/math.sqrt(cov2[3])
    nword=subtract(fsample,transpose(asarray(m3)))
    fcsample=[0,0,0,0]
    fcsample[0]=nword[0]/math.sqrt(cov3[0])
    fcsample[1]=nword[1]/math.sqrt(cov3[1])
    fcsample[2]=nword[2]/math.sqrt(cov3[2])
    fcsample[3]=nword[3]/math.sqrt(cov3[3])

    afsample=dot(fasample,aresults.Wt[:,[0,1]])
    bfsample=dot(fbsample,bresults.Wt[:,[0,1]])
    cfsample=dot(fcsample,cresults.Wt[:,[0,1]])
    pdfa=norm_pdf_multivariate(array(afsample),array(amean),matrix(acov))
    pdfb=norm_pdf_multivariate(array(bfsample),array(bmean),matrix(bcov))
    pdfc=norm_pdf_multivariate(array(cfsample),array(cmean),matrix(ccov))
    pdfmax=max(pdfa,pdfb,pdfc)
    if pdfa==pdfmax:
        write.write("1\n")
        c1+=1
    elif pdfb==pdfmax:
        write.write("2\n")
        c2+=1
    else:
        write.write("3\n")
        c3+=1
print c1
print c2
print c3

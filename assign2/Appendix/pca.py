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
from sklearn.decomposition import PCA
from sklearn import preprocessing
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
write=open("wei8-classified-pca.txt","a")
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
        alst.append(word)
    elif i<=10000:
        blst.append(word)
    else:
        clst.append(word)
#PCA determinie first feature and second feature
aarray=asarray(alst)
barray=array(blst)
carray=asarray(clst)
apca = PCA()
apca.fit(aarray.astype(float))
print(apca.explained_variance_ratio_)
bpca = PCA()
bpca.fit(barray.astype(float))
print(bpca.explained_variance_ratio_)
cpca = PCA()
cpca.fit(carray.astype(float))
print(cpca.explained_variance_ratio_)
# Compute mean and sigma(covariance matrix)
afeature=dot(aarray.astype(float),apca.components_[:,[0,1]])
afeaturef=afeature.astype(float)
amean=mean(afeaturef,0)
acov=cov(afeaturef.T)
bfeature=dot(barray.astype(float),bpca.components_[:,[0,1]])
bfeaturef=bfeature.astype(float)
bmean=mean(bfeaturef,0)
bcov=cov(bfeaturef.T)
cfeature=dot(carray.astype(float),cpca.components_[:,[0,1]])
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
    afsample=dot(fsample,apca.components_[:,[0,1]])
    bfsample=dot(fsample,bpca.components_[:,[0,1]])
    cfsample=dot(fsample,cpca.components_[:,[0,1]])
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

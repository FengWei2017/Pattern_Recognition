# *********************************************************
# Programmer : Feng Wei
# Date: February 7 2017
# Course: ECE8560 Pattern Recognition
# Clemson University School of Computing
# classification program
# First define the Probability Density Function
# Second compute the mean and sigma of each class
# Then reality check use pdf to classify the training data
# Finaly use this model to classify the test data
# **********************************************************
from numpy import *
import math
# Define Probability Density Function


def norm_pdf_multivariate(x, mu, sigma):
    size = len(x)
    if size == len(mu) and (size, size) == sigma.shape:
        det = linalg.det(sigma)
        if det == 0:
            print "error"

        norm_const = 1.0 / (math.pow((2*pi), float(size)/2)
                            * math.pow(det, 1.0/2))
        x_mu = matrix(x - mu)
        inv = sigma.I
        result = math.pow(math.e, -0.5 * (x_mu * inv * x_mu.T))
        return norm_const * result
    else:
        print "error"


# Read train data test data, and open a file to write result
write = open("wei8-classified-takehome1.txt", "a")
train = open("train_sp2017_v19", "r")
test = open("test_sp2017_v19", "r")
trainlines = train.readlines()
testlines = test.readlines()
alst = []
blst = []
clst = []
testlst = []
i = 0
for line in testlines:
    word = line.split()
    testlst.append(word)
testarray = asarray(test)
for line in trainlines:
    i += 1
    word = line.split()
    if i <= 5000:
        alst.append(word)
    elif i <= 10000:
        blst.append(word)
    else:
        clst.append(word)
# Compute mean and sigma(covariance matrix)
aarray = transpose(asarray(alst))
barray = transpose(asarray(blst))
carray = transpose(asarray(clst))
acov = cov(aarray)
afloat = aarray.astype(float)
amean = mean(afloat, 1)
bcov = cov(barray)
bfloat = barray.astype(float)
bmean = mean(bfloat, 1)
ccov = cov(carray)
cfloat = carray.astype(float)
cmean = mean(cfloat, 1)
# Uncorrelated Components
acov = diag(acov.diagonal())
bcov = diag(bcov.diagonal())
ccov = diag(ccov.diagonal())
print acov
print bcov
print ccov
# check reality
c1c1 = 0
c1c2 = 0
c1c3 = 0
c2c1 = 0
c2c2 = 0
c2c3 = 0
c3c1 = 0
c3c2 = 0
c3c3 = 0
for sample in alst:
    tsample = transpose(asarray(sample))
    fsample = tsample.astype(float)
    pdfa = norm_pdf_multivariate(array(fsample), array(amean), matrix(acov))
    pdfb = norm_pdf_multivariate(array(fsample), array(bmean), matrix(bcov))
    pdfc = norm_pdf_multivariate(array(fsample), array(cmean), matrix(ccov))
    pdfmax = max(pdfa, pdfb, pdfc)
    if pdfa == pdfmax:
        c1c1 += 1
    elif pdfb == pdfmax:
        c1c2 += 1
    else:
        c1c3 += 1
for sample in blst:
    tsample = transpose(asarray(sample))
    fsample = tsample.astype(float)
    pdfa = norm_pdf_multivariate(array(fsample), array(amean), matrix(acov))
    pdfb = norm_pdf_multivariate(array(fsample), array(bmean), matrix(bcov))
    pdfc = norm_pdf_multivariate(array(fsample), array(cmean), matrix(ccov))
    pdfmax = max(pdfa, pdfb, pdfc)
    if pdfa == pdfmax:
        c2c1 += 1
    elif pdfb == pdfmax:
        c2c2 += 1
    else:
        c2c3 += 1
for sample in clst:
    tsample = transpose(asarray(sample))
    fsample = tsample.astype(float)
    pdfa = norm_pdf_multivariate(array(fsample), array(amean), matrix(acov))
    pdfb = norm_pdf_multivariate(array(fsample), array(bmean), matrix(bcov))
    pdfc = norm_pdf_multivariate(array(fsample), array(cmean), matrix(ccov))
    pdfmax = max(pdfa, pdfb, pdfc)
    if pdfa == pdfmax:
        c3c1 += 1
    elif pdfb == pdfmax:
        c3c2 += 1
    else:
        c3c3 += 1

print c1c1
print c2c2
print c3c3
total = c1c1+c2c2+c3c3
print total/15000.0
# classify test data
c1 = 0
c2 = 0
c3 = 0
for sample in testlst:
    tsample = transpose(asarray(sample))
    fsample = tsample.astype(float)
    pdfa = norm_pdf_multivariate(array(fsample), array(amean), matrix(acov))
    pdfb = norm_pdf_multivariate(array(fsample), array(bmean), matrix(bcov))
    pdfc = norm_pdf_multivariate(array(fsample), array(cmean), matrix(ccov))
    pdfmax = max(pdfa, pdfb, pdfc)
    if pdfa == pdfmax:
        write.write("1\n")
        c1 += 1
    elif pdfb == pdfmax:
        write.write("2\n")
        c2 += 1
    else:
        write.write("3\n")
        c3 += 1
print c1
print c2
print c3

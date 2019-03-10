# *********************************************************
# Programmer : Feng Wei
# Date: March 7 2017
# Course: ECE8560 Pattern Recognition
# Clemson University School of Computing
# classification program
# First define the H-k Function
# Compute Wab Wac Wbc
# Finaly use this model to classify the test data
# **********************************************************
from numpy import *
import math
import numpy.linalg


def findE(x, b):
    x_inv = numpy.linalg.pinv(x)
    W = numpy.dot(x_inv, b)
    E = numpy.subtract(numpy.dot(x, W), b)
    enm = 0
    E_rounded = numpy.around(E.astype(numpy.double), 1)
    return E_rounded, W


def checkEEZ(E):
    for row in E:
        if (row != 0):
            return False
    return True


def checkELZ(E):  # Check if the matrix "E" is less than zero
    for row in E:
        if (row > 0 or row == 0):
            return False
    return True


# Read train data test data, and open a file to write result
write = open("wei8-classified-hk.txt", "a")
train = open("train_sp2017_v19", "r")
test = open("test_sp2017_v19", "r")
trainlines = train.readlines()
testlines = test.readlines()
alst = []
b1lst = []
b2lst = []
clst = []
testlst = []
i = 0
for line in testlines:
    word = line.split()
    word = [float(x) for x in word]
    testlst.append(word)
testarray = asarray(test)
for line in trainlines:
    i += 1
    word = line.split()
    word = [float(x) for x in word]
    if i <= 5000:
        alst.append(word)
    elif i <= 10000:
        b2lst.append(word)
        word = [-x for x in word]
        b1lst.append(word)
    else:
        word = [-x for x in word]
        clst.append(word)
# lst to array
alst = [x+[1] for x in alst]
b1lst = [x+[-1] for x in b1lst]
b2lst = [x+[1] for x in b2lst]
clst = [x+[-1] for x in clst]
testlst = [x+[1] for x in testlst]
ablst = alst+b1lst
aclst = alst+clst
bclst = b2lst+clst
nab = 0
nac = 0
nbc = 0
# compute h-k
ab = [1 for x in ablst]
abflag = 1
acflag = 1
bcflag = 1
while (abflag):
    Eab, Wab = findE(ablst, ab)
    EEZ = checkEEZ(Eab)
    ELZ = checkELZ(Eab)
    if (EEZ):
        print "ab solution is possible"
        abflag = 0
        break
    elif (ELZ):
        print "ab No solution is possible"
        abflag = 0
        break
    nab += 1
    if nab > 100:
        abflag = 0
    ab = numpy.add(ab, numpy.add(Eab, numpy.absolute(Eab)))
ac = [1 for x in aclst]
while (acflag):  # Keep running until we find a solution or a solution is not possible
    Eac, Wac = findE(aclst, ac)
    EEZ = checkEEZ(Eac)
    ELZ = checkELZ(Eac)
    if (EEZ):
        print "ac solution is possible"
        acflag = 0
        break
    elif (ELZ):
        print "ac No solution is possible"
        acflag = 0
        break
    nac += 1
    if nac > 100:
        acflag = 0
    # Add b to the addition of E and the absolute value of E
    ac = numpy.add(ac, numpy.add(Eac, numpy.absolute(Eac)))
bc = [1 for x in bclst]
while (bcflag):  # Keep running until we find a solution or a solution is not possible
    Ebc, Wbc = findE(bclst, bc)
    EEZ = checkEEZ(Ebc)
    ELZ = checkELZ(Ebc)
    if (EEZ):
        print "bc olution is possible"
        bcflag = 0
        break
    elif (ELZ):
        print "bc No solution is possible"
        bcflag = 0
        break
    nbc += 1
    if nbc > 1000:
        bcflag = 0
    # Add b to the addition of E and the absolute value of E
    bc = numpy.add(bc, numpy.add(Ebc, numpy.absolute(Ebc)))

# *************************************************
print Wab
print Wac
print Wbc
# classify test data
c1 = 0
c2 = 0
c3 = 0
for sample in testlst:
    tsample = transpose(asarray(sample))
    fsample = tsample.astype(float)
    dotab = dot(Wab, fsample)
    dotac = dot(Wac, fsample)
    dotbc = dot(Wbc, fsample)
    if dotab > 0 and dotac > 0:
        write.write("1\n")
        c1 += 1
    elif dotbc > 0:
        write.write("2\n")
        c2 += 1
    else:
        write.write("3\n")
        c3 += 1
print c1
print c2
print c3

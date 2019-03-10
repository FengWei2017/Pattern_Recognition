# *********************************************************
# Programmer : Feng Wei
# Date: February 7 2017
# Course: ECE8560 Pattern Recognition
# Clemson University School of Computing
# Test Perror
# **********************************************************/
test = open("wei8-classified-takehome1.txt", "r")
testlines = test.readlines()
testlst = []
answerlst = []
for line in testlines:
    testlst.append(int(line))
for i in range(2500):
    answerlst.append(3)
    answerlst.append(1)
    answerlst.append(2)
    answerlst.append(3)
    answerlst.append(2)
    answerlst.append(1)
print len(testlst)
print len(answerlst)
errorlst = []
for a in range(15000):
    error = testlst[a]-answerlst[a]
    errorlst.append(error)
print errorlst.count(0)
b = errorlst.count(0)
print 1-b/15000.0

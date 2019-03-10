#*********************************************************
# Programmer : Feng Wei
# Date: March 10 2017
# Course: ECE8560 Pattern Recognition
# Clemson University School of Computing
# Test Perror
#**********************************************************/
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
c1c1 = 0
c1c2 = 0
c1c3 = 0
c2c1 = 0
c2c2 = 0
c2c3 = 0
c3c1 = 0
c3c2 = 0
c3c3 = 0
for a in range(15000):
    if answerlst[a] == 1:
	if testlst[a] == 1:
	    c1c1 += 1
	elif testlst[a] == 2:
	    c1c2 += 1
	else:
	    c1c3 += 1
    elif answerlst[a] == 2:
	if testlst[a] == 1:
	    c2c1 += 1
	elif testlst[a] == 2:
	    c2c2 += 1
	else:
	    c2c3 += 1
    else:
	if testlst[a] == 1:
	    c3c1 += 1
	elif testlst[a] == 2:
	    c3c2 += 1
	else:
	    c3c3 += 1
print c1c1
print c1c2
print c1c3
print c2c1
print c2c2
print c2c3
print c3c1
print c3c2
print c3c3
print (c1c1+c2c2+c3c3)/15000.0

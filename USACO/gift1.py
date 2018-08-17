"""
ID: pengsha2
LANG: PYTHON3
PROG: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
NP = int(fin.readline().strip())#reading the first line
myDict = {}#initializing name dict
for i in range(NP):#cunstructing the dictionary with names and their money
	name = fin.readline().strip()
	myDict[name] = 0
print(myDict, len(myDict))
for i4 in range(NP):
	grpName = fin.readline().strip()
	grpMon = fin.readline().strip().split(" ")
	print(grpMon)
	totalMon = int(grpMon[0])
	toDivide = int(grpMon[1])
	if toDivide == 0:
		moneyEach = 0
	else:
		moneyEach = totalMon//toDivide
	moneyTotal = moneyEach*toDivide
	myDict[grpName] -= moneyTotal
	for i1 in range(toDivide):
		name1 = fin.readline().strip()
		myDict[name1] += moneyEach
for names in myDict:
	fout.write(names + ' ' + str(myDict[names]) + '\n')
fout.close()

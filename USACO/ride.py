"""
ID: pengsha2
LANG: PYTHON3
PROG: ride
"""
import string
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
comet = fin.readline().strip()
group = fin.readline().strip()
alpha = list(string.ascii_uppercase)
cometNum = 1
groupNum = 1
for c in comet:
	cometNum *= (alpha.index(c) + 1)
for g in group:
	groupNum *= (alpha.index(g) + 1)
if cometNum%47 == groupNum%47:
	output = "GO"
else:
	output = "STAY"
fout.write (output + '\n')
fout.close()

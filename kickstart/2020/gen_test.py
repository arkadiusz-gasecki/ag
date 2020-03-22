import random

f = open('inp.txt','w')

for i in range(1,3001):
    Ai = random.randint(1,1000)
    f.write(str(Ai)+ ' ');

f.close()

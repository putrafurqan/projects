
import random
import datetime
for i in range(5):
    randnum = []
    for i in range(1000000):
        g = random.randint(1,1000000000)
        randnum.append(g)
    start = str(datetime.datetime.now())
    randnum = sorted(randnum)
    end = str(datetime.datetime.now())
    print("sorted() Delay(sec) : " + str(float(end[17:])-float(start[17:])))
    

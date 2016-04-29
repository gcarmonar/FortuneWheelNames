import time
import random

print ("F O R T U N E   W H E E L !")
random.seed(time.clock)

names = ["Gerardo", "Luis", "Steve", "Tyler", "John"]
print (names)
order = []

for i in range (len(names)):
	for j in range (4):
		rnd = random.randrange(0, len(names))
		print (names[rnd])
		time.sleep(1)
	rnd = random.randrange(0, len(names))
	print ("--The winner ->", i+1, names[rnd])
	print ()
	order.append(names[rnd])
	time.sleep(3)
	del names[rnd]
	
print (order)

from random import randint

m = str()
for i in range(3):
	if i == 0:
		m += str(randint(10,20))
	else:
		m += str(randint(1,3))
	if i != 2:
		m += "-"
	else:
		m += "\n"
print(m)
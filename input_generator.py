import random

num1 = '1' + "".join(str(random.randint(0, 1)) for x in range(2048 - 2)) + '1'
num2 = '1' + "".join(str(random.randint(0, 1)) for x in range(1024 - 2)) + '1'

f = open("./num1.txt", 'rb+')
f.write(num1.encode())
f.close()

f = open("./num2.txt", 'rb+')
f.write(num2.encode())
f.close()

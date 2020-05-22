import random
import time
  
def powerMod(x, y, p):       
  res = 1

  x = x % p
  while (y > 0): 
    if (y & 1): 
      res = (res * x) % p
    y = y >> 1
    x = (x * x) % p
      
    return res; 
  
def millerRabin(r, n): 
  a = random.randint(2, n - 2)
  y = powerMod(a, r, n)
  
  if (y != 1 and y != n - 1): 
    while (r != n - 1): 
      y = (y*y) % n
      r *= 2
      if y == 1: 
        return False
      if y == n - 1: 
        return True
  else:
    return True
  
  return False

def testPrime(n, t): 

  k = n - 1
  while (k % 2 == 0): 
    k //= 2

  while t >= 0:
    t = t - 1
    if millerRabin(k, n) == False: 
      return False

  return True

def generateNum(length):
  res = 0b1
  while length > 2:
    res = res << 1 | random.choice([0b0, 0b1])
    length = length - 1
  res = res << 1 | 0b1

  return res

if __name__ == '__main__':
  t = 3

  print()

  begin = time.process_time()
  num1 = generateNum(1024)
  f = open("./num1.txt", 'rb+')
  f.write(bin(num1).encode())
  f.close()
  if testPrime(num1, t):
    print("RESULT: num1 is a prime number")
  else:
    print("RESULT: num1 is not a prime number")
  end = time.process_time()
  print("DURATION: " + str(end-begin))

  print()

  begin = time.process_time()
  num2 = generateNum(2048)
  f = open("./num2.txt", 'rb+')
  f.write(bin(num2).encode())
  f.close()
  if testPrime(num2, t):
    print("RESULT: num2 is a prime number")
  else:
    print("RESULT: num2 is not a prime number")
  end = time.process_time()
  print("DURATION: " + str(end-begin))

  # if testPrime(num2, t):
  #   print("Num2 is a Prime Number")
  # else:
  #   print("Num2 is not a Prime Number")

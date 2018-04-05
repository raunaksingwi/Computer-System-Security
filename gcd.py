def gcd(a,b):
  
  if a == 0:
    return b

  if b == 0:
    return a

  while True:
    r = a % b
    a = b
    b = r

    if r == 0:
      break

  return a

def hasInverse(a,b):
  if gcd(a, b) == 1:
    return True

def main():
  #print(gcd(15,5))



if __name__ == '__main__':
  main()


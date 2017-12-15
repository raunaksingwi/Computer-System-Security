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

def main():
  print(gcd(15,5))
  print(gcd(11,0))
  print(gcd(0,12))
  print(gcd(6,4))
  print(gcd(12,6))


if __name__ == '__main__':
  main()


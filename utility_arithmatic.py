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


def extended_euclidean(n,b):
  r1 = n
  r2 = b
  t1 = 0
  t2 = 1

  while r2 > 0:
    q = r1/r2
    r = r1 - q * r2
    r1 = r2
    r2 = r
    t = t1 - q * t2
    t1 = t2
    t2 = t

  return (t1 % n)

def main():
  print(extended_euclidean(26,11))
  #print(gcd(26,11))


if __name__ == '__main__':
  main()
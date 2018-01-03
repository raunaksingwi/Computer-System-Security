def fast_exponentiation(a,e,n):
  e = bin(e)[2:]
  e = e[::-1]
  y = 1
  for i in range(len(e)):
    if e[i] == '1':
      y = (y * a) % n

    a = a**2 % n
  return y

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

def is_relatively_prime(a,b):
  if gcd(a, b) == 1:
    return True
  else:
    return False

def extended_euclidean(n,b):
  r1 = n
  r2 = b
  t1 = 0
  t2 = 1

  while r2 > 0:
    q = r1//r2
    r = r1 - q * r2
    r1 = r2
    r2 = r
    t = t1 - q * t2
    t1 = t2
    t2 = t

  return (t1 % n)

def chainese_remainder(a1,a2,m1,m2):
  M = m1 * m2

  M1 = M//m1
  M2 = M//m2

  M1_INVERSE = extended_euclidean(m1, M1)
  M2_INVERSE = extended_euclidean(m2, M2)

  x = (a1 * M1 * M1_INVERSE + a2 * M2 * M2_INVERSE) % M
  return x

def main():
  print(extended_euclidean(26,11))

if __name__ == '__main__':
  main()
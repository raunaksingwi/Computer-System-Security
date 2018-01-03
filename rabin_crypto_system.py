from utility_arithmatic import *

def key_generation():
  global p,q,n
  p = 7
  q = 11
  n = p * q

def encryption(P):
  return (P**2) % n


def decryption(C):
  a1 = fast_exponentiation(C, (p+1)//4, p)
  a2 = -fast_exponentiation(C, (p+1)//4, p)
  b1 = fast_exponentiation(C, (q+1)//4, q)
  b2 = -fast_exponentiation(C, (q+1)//4, q)

  p1 = chainese_remainder(a1, b1, p, q)
  p2 = chainese_remainder(a1, b2, p, q)
  p3 = chainese_remainder(a2, b1, p, q)
  p4 = chainese_remainder(a2, b2, p, q)

  return (p1,p2,p3,p4)



def main():
  key_generation()
  P = 5
  print("The plaintext is",P)
  C = encryption(P)
  print("The ciphertext is",C)
  print("The possible values of plaintext after decryption are :")
  P = decryption(C)

  for i in P:
    print(i)


if __name__ == '__main__':
  main()
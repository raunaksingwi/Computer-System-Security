#ElGamal Cryptography System.
from utility_arithmatic import *

def key_generation():
  global p,e1,e2,d
  p = 13
  d = 7
  e1 = primitive_roots(p)[0]
  e2 = fast_exponentiation(e1, d, p)


def encryption(P):
  r = 5
  C1 = fast_exponentiation(e1, r, p)
  #C2 = (P* e**r)mod P
  C2 = ((P % p) * (fast_exponentiation(e2,r,p))) % p

  return (C1,C2)

def decryption(C):
  C1 = C[0]
  C2 = C[1]

  return (C2 * (extended_euclidean(p,fast_exponentiation(C1,d,p)))) % p

def main():
  P = 5
  print("Plaintext =",P)
  key_generation()
  C = encryption(P)
  print("Ciphertext =",C)
  P = decryption(C)
  print("Decrypted Plaintext =",P)


if __name__ == '__main__':
  main()
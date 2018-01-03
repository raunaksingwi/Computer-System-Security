from utility_arithmatic import *

def RSA_key_generation():
  global e,n,d
  p = 7
  q = 11
  n = p * q
  fi_n = (p - 1) * (q - 1)
  e = 13
  d = extended_euclidean(fi_n, e)

def RSA_encryption(P):
  return fast_exponentiation(P, e, n)

def RSA_decryption(C):
  return fast_exponentiation(C, d, n)

def main():
  RSA_key_generation()
  P = 5
  print("Plain text before encryption",P)
  C = RSA_encryption(P)
  print("Ciphertext is ",C)
  P = RSA_decryption(C)
  print("Decrypted text",P)

if __name__ == '__main__':
  main()
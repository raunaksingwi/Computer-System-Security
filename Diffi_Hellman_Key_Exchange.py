#Diffi Hellman Key Exchange Agreement

from utility_arithmatic import *
global g,p,x,y,R1,R2


def UserA_generation():
  global x,R1
  x = 3 #should be p - a random number
  R1 = fast_exponentiation(g,x,p)

def UserB_generation():
  global y,R2
  y = 6 #should be p - a random number
  R2 = fast_exponentiation(g,y,p)

def UserA_exchange():
  Kab = fast_exponentiation(R2, x, p)
  print("User A has calculated the key Kab as",Kab)

def UserB_exchange():
  global R1,y,p
  Kab = fast_exponentiation(R1, y, p)
  print("User A has calculated the key Kab as",Kab)

def main():
  global p,g
  p = 23
  #g = primitive_roots(p)[0]
  g = 7
  UserA_generation()
  UserB_generation()
  UserA_exchange()
  UserB_exchange()


if __name__ == '__main__':
  main()
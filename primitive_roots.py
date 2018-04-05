from utility_arithmatic import is_relatively_prime

def primitive_roots(p):
  #p = int(input("Enter the P in Zp*\n"))
  Zn = [int(i) for i in range(1,p)]
  Zp = []

  for element in Zn:
    if is_relatively_prime(element, p) == 1:
      Zp.append(element)

  total_elements = len(Zp)
  primitive_roots = []

  for a in Zp:
    group = set()
    for n in Zn:
      group.add(pow(a,n)%p)
    if len(group) == total_elements:
      primitive_roots.append(a)

  return primitive_roots

def main():
  roots = primitive_roots(10)
  print(roots)
if __name__ == '__main__':
  main()
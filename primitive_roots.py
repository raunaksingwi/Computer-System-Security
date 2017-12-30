from utility_arithmatic import is_relatively_prime

def main():
  #p = int(input("Enter the P in Zp*\n"))
  p = 10
  Zn = [int(i) for i in range(1,p)]
  Zp = []

  for element in Zn:
    if is_relatively_prime(element, p) == 1:
      Zp.append(element)

  total_elements = len(Zp)

  for a in Zp:
    group = set()
    for n in Zn:
      group.add(pow(a,n)%p)
    if len(group) == total_elements:
      print(a, "is a primitive root.")

if __name__ == '__main__':
  main()
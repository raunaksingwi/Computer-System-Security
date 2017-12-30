def XOR(result,irreducable_polynomial):

  xor_result = ""

  for i in range(len(result)):

    if result[i] == irreducable_polynomial[i]:
      xor_result += '0'
    else:
      xor_result += '1'

  return xor_result



def multiply(polynomial1,polynomial2,irreducable_polynomial):

  global result_array

  result = polynomial2

  for _ in range(len(str(int(polynomial1))) - 1):

    if result[0] == '0':
      result = result[1:] + '0'
    else:
      result = result[1:] + '0'
      result = XOR(result,irreducable_polynomial)
    result_array.append(result)


def main():
  global result_array
  result_array = []
  polynomial1 = input("Enter the first polynomial\n")
  polynomial2 = input("Enter the second polynomial\n")
  irreducable_polynomial = input("Enter the irreducable polynomial\n")[1:]

  if len(polynomial1) != len(polynomial2):
    print("BAD INPUT")


  multiply(polynomial1, polynomial2, irreducable_polynomial)
  result_array.reverse()
  print(result_array)
  desired_results = []

  polynomial1 = str(int(polynomial1))

  for i in range(len(polynomial1)):
    if polynomial1[i] == '1':
      desired_results.append(result_array[i])

  #print(desired_results)

  prev_result = '00000000'
  for expression in desired_results:
    result = XOR(expression, prev_result)
    prev_result = result

  print(result)

if __name__ == '__main__':
  main()
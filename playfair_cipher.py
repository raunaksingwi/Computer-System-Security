def search2d(list,element):
  for i in range(len(list)):
    for j in range(len(list[0])):
      if element == list[i][j]:
        return i,j


def encrypter(plain_text,key):

  cipher_text = ""

  alphabet_set = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for ch in key:
    if ch == 'j':
      alphabet_set.remove('i')
    alphabet_set.remove(ch)

  for ch in key[::-1]:
    alphabet_set.insert(0, ch)

  counter = 0
  matrix = []
  temp = []
  for ch in alphabet_set:
    counter += 1
    temp.append(ch)

    if counter == 5:
      matrix.append(temp)
      temp = []
      counter = 0

  filtered_plain_text = ""
  i = 0
  while i < len(plain_text):
    filtered_plain_text += plain_text[i]
    if plain_text[i] == plain_text[i+1]:     
      filtered_plain_text += 'x'
    filtered_plain_text += plain_text[i+1]

    i += 2
    if i == (len(plain_text)-1):
      filtered_plain_text += plain_text[i]
      break


  if len(filtered_plain_text) % 2 != 0:
    filtered_plain_text += 'x'

  print(filtered_plain_text)

  for i in range(0,len(filtered_plain_text),2):
    first_i,first_j = search2d(matrix, filtered_plain_text[i])
    second_i,second_j = search2d(matrix, filtered_plain_text[i+1])

    if first_j == second_j:
      cipher_text += matrix[(first_i+1)%5][first_j]
      cipher_text += matrix[(second_i+1)%5][second_j]

    elif first_i == second_i:
      cipher_text += matrix[first_i][(first_j+1)%5]
      cipher_text += matrix[second_i][(second_j+1)%5]

    else:
      cipher_text += matrix[first_i][second_j]
      cipher_text += matrix[second_i][first_j]

  return cipher_text



def decrypter(cipher_text):
  pass

def main():
  print(encrypter("iaminseventhsem", "eight").upper())

#ba lx lo wn
if __name__ == '__main__':
  main()

def numeric_value(ch): return ord(ch) - 97

def encrypter(plain_text):

  a = 7
  b = 2
  cipher_text = ""
  
  for ch in plain_text:
    if ch == " ": continue
    cipher_text += chr(((numeric_value(ch) * a  + b) % 26) + 97)

  return cipher_text

def decrypter(cipher_text):
  a_inverse = 15
  b = 2
  plain_text = ""
  for ch in cipher_text:
    plain_text += chr((((numeric_value(ch) - b) * a_inverse) % 26) + 97)
  return plain_text


def main():
  plain_text = "hello"
  cipher_text = encrypter(plain_text)
  print(cipher_text.upper())
  plain_text = decrypter(cipher_text)
  print(plain_text)


if __name__ == '__main__':
  main()
def menu():
  print("SECRET DECODER MENU")
  response = input("""

    0) Quit
    1) Encode
    2) Decode
What is your choice?: """)
  return response

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"


def encode(plain):
  output = ""
  plain = plain.upper()
  for letter in plain:
    if letter in key:
      index = alpha.find(letter)
      translated = key[index]
      output = output + translated
  return output

def decode(coded):
  output = ""
  coded = coded.upper()
  for letter in coded:
    if letter in key:
      index = key.find(letter)
      translated = alpha[index]
      output = output + translated
  return output


def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = input("text to be encoded: ")
      print(encode(plain))
    elif response == "2":
      coded = input("code to be decyphered: ")
      print (decode(coded))
    elif response == "0":
      print ("Thanks for doing secret spy stuff with me.")
      keepGoing = False
    else:
      print ("I don't know what you want to do...")

#my starter code.

if __name__ == "__main__":

  main()

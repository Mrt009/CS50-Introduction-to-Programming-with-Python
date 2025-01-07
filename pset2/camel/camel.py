
# make function to make code clear and systematic
def convert(variable):
    # for loop is used to check the state of each of every character and end is used to avoid the new line
   print("Snake case : ", end="")
   for char in variable:
      if char.isupper():
         print(f"_{char.lower()}",end="")
      else:
          print(char,end="")

def main():
    response= input("Provide the variable in camelCase: ")
    convert(response)

main()
print("\n")
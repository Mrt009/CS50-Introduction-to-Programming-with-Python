


def main():
 #To get response from the user
 i_response=input("Greeting:  ")
# To ignore whitespaces and case sensitivity
 response= i_response.lower().replace(" ","")
 value(response)


def value(greeting):
    if greeting.startswith("hello"):
      print("$0")
    elif greeting.startswith("h"):
      print("$20")
    else:
      print("$100")


if __name__ == "__main__":
    main()

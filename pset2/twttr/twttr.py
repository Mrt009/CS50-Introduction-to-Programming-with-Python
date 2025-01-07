def response():
    i_response = input("Enter input: ")

    loop(i_response)





def loop(response):
        for char in response:
            if char =="a" or  char =="e"or  char =="i"or char =="o"or char =="u" or char =="A" or  char =="E"or  char =="I"or char =="O"or char =="U":
                print("", end="")

            else:
                print(char,end ="")
response()
print("\n")

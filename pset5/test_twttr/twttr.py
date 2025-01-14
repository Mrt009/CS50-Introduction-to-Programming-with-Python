def main():
    i_response = input("Enter input: ")

    shorten(i_response)


def shorten(word):
     for char in word:
            if char =="a" or  char =="e"or  char =="i"or char =="o"or char =="u" or char =="A" or  char =="E"or  char =="I"or char =="O"or char =="U":
                print("", end="")

            else:
                print(char,end ="")


if __name__ == "__main__":
    main()




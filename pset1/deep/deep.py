#taking answer for the user
i_answer=input("What is the answer to the Great Question of Life, the Universe and Everything: ")
#replace is used to remove whitespaces and lower is used to convert the response of the user to small letters
answer=i_answer.replace(" ","").lower()


#conditions which gives yes for different form of 42
if answer== "fortytwo" or answer ==  '42' or answer== "forty-two":
   print("Yes")
else:
    print("No")
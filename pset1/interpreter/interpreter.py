# to get input from the user
response=input("Enter the experession in this format: value <space> operator <space> value:  ")
"""to divide the provided input into first value, operator sign and second value and also assigning the fist value into variable and float is used to convert given string into float """
inital_value= float(response.split()[0])
#asigning the operator  in the variable
operator = response.split()[1]
#asigning the second value in the variable
second_value = float(response.split()[2])



#condition apply

if operator =="+":
    print(inital_value + second_value)

elif operator =="-":
    print(inital_value - second_value)
elif operator =="*":
    print(inital_value * second_value)
elif operator =="/":
    print(inital_value / second_value)
else:
    print("input error, try again 😊")
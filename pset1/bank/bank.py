#To get response from the user
i_response=input("Greeting:  ")
# To ignore whitespaces and case sensitivity
response= i_response.lower().replace(" ","")
# Condition appy to get desired outcomes, and startswith is used to validate the start part so that we can compare with condition
if response.startswith("hello"):
    print("$0")
elif response.startswith("h"):
    print("$20")
else:
    print("$100")
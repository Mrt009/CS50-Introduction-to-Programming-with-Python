
# taking input from the user and converting it to small letter also removing the whitespaces
file_name=input("File Name:  ").replace(" ","").lower()
#apply condition and using endswith to compare the end part of the user response
if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg")or file_name.endswith(".jpeg"):
     print("image/jpeg")


elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".zip"):
    print("application/zip")
elif file_name.endswith(".png"):
     print("image/png")
elif file_name.endswith(".txt"):
     print("text/plain")
else:
  print("application/octet-stream")
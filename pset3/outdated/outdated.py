

calendar = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}
while True:
 try:
    response = input("Date: ").strip()

    # Check if input starts with an alphabetic character
    if response[0].isalpha():
         # Check if the input has a comma separating day and year
        if ',' not in response:
            raise ValueError("Comma missing between day and year.")

        month, day, year = response.split(" ")
        if day.isalnum():
            raise ValueError
        day =day.replace(",","")

        month = month.title()  # Capitalize month
    else:
        month, day, year = response.split("/")
        month = month.zfill(2)# Ensure month is two digits
        if not (1 <= int(month) <= 12):
            raise ValueError("Invalid month.")


    day = day.zfill(2)  # Ensure day is two digits
    # Check if the day is within a valid range (1-31)
    if not (1 <= int(day) <= 31):
        raise ValueError("Invalid day.")  # Reject invalid day


    # Validate and convert month
    for key, value in calendar.items():
        if month == key or month == value:
            print(f"{year}-{value}-{day}")
            break
    break

   

 except ValueError:
    print("Invalid data provided.")

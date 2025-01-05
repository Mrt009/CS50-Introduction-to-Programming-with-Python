


def main():
    response = input("What is the time: ")
    final_time = convert(response)

    if 7.0 <= final_time <= 8.0:
        print("Breakfast time")
    elif 12.0 <= final_time <= 13.0:
        print("Lunch time")
    elif 18.0 <= final_time <= 19.0:
        print("Dinner time")

def convert(time):
    # Convert time in HH:MM format to a float value representing the time in hours
    hrs_time, min_time = time.split(":")
    final_time = float(hrs_time) + float(min_time) / 60
    return final_time

if __name__ == "__main__":
    main()

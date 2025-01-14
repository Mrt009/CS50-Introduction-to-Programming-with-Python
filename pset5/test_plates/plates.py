

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and first_two(s) and special_char(s)and zero(s)  and near(s):
        return True
    else:
        return False


def length(s):
    # Length must be between 2 and 6 characters
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def first_two(s):
    # First two characters must be alphabetic
    if s[0:2].isalpha():
        return True
    else:
        return False


def special_char(s):
    # Ensure no special characters
    for char in s:
        if  not char.isalnum():
            return False
        else:

            return True



def zero(s):
    # The first number in the plate cannot be '0'
    for char in s:
        if char.isdigit():
            if char == '0':
                return False
            break  # Stop after checking the first digit
    return True


def near(s):
    # Ensure numbers appear only at the end of the plate
    for i, char in enumerate(s):
        if char.isdigit():
            return s[i:].isdigit()  # All characters from this point must be digits
    return True  # No numbers found



if __name__ == "__main__":
    main()


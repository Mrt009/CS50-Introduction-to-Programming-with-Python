def main():
    am_due = 50
    while am_due > 0:
        i_coin = input("Insert Coin: ")
        coin = int(i_coin)
        coin = accept(coin)
        if coin > 0:  # Only subtract if a valid coin was inserted
            am_due -= coin
        if am_due <= 0:
            break  # Exit loop once amount is fully paid
        print(f"Amount Due: {max(am_due, 0)}")  # Ensure no negative values
    print(f"Change Owed: {abs(am_due)}")  # Show change if overpaid

def accept(coin):
    if coin == 25 or coin == 10 or coin == 5:
        return coin
    else:
        print("Sorry, we don't accept this coin")
        return 0

main()

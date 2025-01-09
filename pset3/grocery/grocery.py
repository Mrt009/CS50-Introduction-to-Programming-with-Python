
# Dictionary to store items and their counts
items = {}

while True:
    try:
        # Read input and convert to uppercase
        item = input().strip().upper()

        # Increment count if item exists, otherwise add it with count 1
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        # Sort items alphabetically
        sorted_items = sorted(items.items())

        # Print each item and its count
        for item, count in sorted_items:
            print(f"{count} {item}")
        break

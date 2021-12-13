book = input()
count = 0

while True:
    new_book = input()

    if book == new_book:
        print(f"You checked {count} books and found it.")
        break

    elif new_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count} books.")
        break

    count += 1
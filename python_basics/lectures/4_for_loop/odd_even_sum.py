number = int(input())
odd_number = 0
even_number = 0

for num in range(number):
    current_number = int(input())

    if num % 2 == 0:
        even_number += current_number
    else:
        odd_number += current_number

if even_number == odd_number:
    print("Yes")
    print(f"Sum = {even_number}")

else:
    res = abs(even_number - odd_number)
    print("No")
    print(f"Diff = {res}")




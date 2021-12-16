command = input()
prime_numbers_sum = 0
non_prime_numbers_sum = 0
int_command = ""


while command != "stop":

    int_command = int(command)

    if int_command < 0:
        print("Number is negative.")

    else:
        number_is_prime = True
        for x in range(2, int_command):
            if int_command % x == 0:
                number_is_prime = False
                break

        if number_is_prime:
            prime_numbers_sum += int_command
        else:
            non_prime_numbers_sum += int_command

    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
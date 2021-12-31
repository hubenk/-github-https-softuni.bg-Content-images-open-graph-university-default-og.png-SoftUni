year = int(input())

while True:
    year += 1
    string_year = str(year)

    for x in range(len(string_year)):
        test_digit = string_year[x]
        for y in range(x + 1, len(string_year)):
            second_test_digit = string_year[y]
            for z in range(y + 1, len(string_year)):
                third_test_digit = string_year[z]
                for q in range(z + 1, len(string_year)):
                    fourth_test_digit = string_year[q]
                    new_year = test_digit + second_test_digit + third_test_digit + fourth_test_digit
                    if len(set(new_year)) == len(string_year):
                        print(string_year)
                        exit()

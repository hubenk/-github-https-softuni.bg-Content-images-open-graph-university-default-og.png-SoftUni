def perfect_number(perf_num):
    sum = 0

    for number in range(1, perf_num):
        if perf_num % number == 0:
            sum += number

    if sum == perf_num:
        return "We have a perfect number!"
    return "It's not so perfect."


test_number = int(input())

print(perfect_number(test_number))


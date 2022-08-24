def fibonacci():
        fib_nums = [0, 1]
        yield fib_nums[0]
        yield fib_nums[1]

        while True:
            sum_nums = sum(fib_nums)
            yield sum_nums
            fib_nums.append(sum_nums)
            fib_nums.pop(0)


generator = fibonacci()
for i in range(5):
    print(next(generator))

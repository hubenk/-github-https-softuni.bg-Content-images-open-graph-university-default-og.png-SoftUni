happiness = input().split()
factor = int(input())
count = []

happiness = [int(number) * factor for number in happiness]
avg_happy = sum(happiness) / len(happiness)
happy_count = [count.append(1) for rate in happiness if int(rate) > avg_happy]

if sum(count) < len(happiness) / 2:
    print(f"Score: {sum(count)}/{len(happiness)}. Employees are not happy!")
else:
    print(f"Score: {sum(count)}/{len(happiness)}. Employees are happy!")

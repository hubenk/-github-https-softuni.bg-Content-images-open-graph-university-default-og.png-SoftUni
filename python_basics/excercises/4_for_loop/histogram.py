n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0


for x in range(n):
    num_in_diapason = int(input())

    if 1 <= num_in_diapason < 200:
        p1 += 1
    elif 200 <= num_in_diapason < 400:
        p2 += 1
    elif 400 <= num_in_diapason < 600:
        p3 += 1
    elif 600 <= num_in_diapason < 800:
        p4 += 1
    else:
        p5 += 1

sum1 = p1 / n * 100
sum2 = p2 / n * 100
sum3 = p3 / n * 100
sum4 = p4 / n * 100
sum5 = p5 / n * 100


print(f"{sum1:.2f}%")
print(f"{sum2:.2f}%")
print(f"{sum3:.2f}%")
print(f"{sum4:.2f}%")
print(f"{sum5:.2f}%")
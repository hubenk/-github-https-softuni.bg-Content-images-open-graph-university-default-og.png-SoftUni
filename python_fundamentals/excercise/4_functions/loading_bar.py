def loading_bar(number):
    percent = number // 10
    dots = 10 - percent

    if number != 100:
        return f"{number}% [" + percent * "%" + dots * "." + "] \nStill loading..."
    return "100% Complete! \n[%%%%%%%%%%]"


percentage = int(input())

print(loading_bar(percentage))


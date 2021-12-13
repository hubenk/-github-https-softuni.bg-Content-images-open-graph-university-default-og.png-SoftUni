bill = float(input())
bill = int(bill * 100)
coins = 0

coins += bill // 200
bill = bill % 200

coins += bill // 100
bill = bill % 100

coins += bill // 50
bill = bill % 50

coins += bill // 20
bill = bill % 20

coins += bill // 10
bill = bill % 10

coins += bill // 5
bill = bill % 5

coins += bill // 2
bill = bill % 2

coins += bill // 1


print(coins)
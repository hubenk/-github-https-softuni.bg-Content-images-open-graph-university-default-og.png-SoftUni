load = int(input())
bus = 0
bus_tons = 0
truck = 0
truck_tons = 0
train = 0
train_tons = 0
total_tons = 0

for weight in range(1, load + 1):
    tons = int(input())
    if tons <= 3:
        bus += 200 * tons
        bus_tons += tons
    elif tons <= 11:
        truck += 175 * tons
        truck_tons += tons
    elif tons >= 12:
        train += 120 * tons
        train_tons += tons
    total_tons += tons

total_expense = bus + truck + train
avg_per_tone = total_expense / total_tons

bus_percnt = bus_tons / total_tons * 100
truck_percnt = truck_tons / total_tons * 100
train_percnt = train_tons / total_tons * 100

print(f"{avg_per_tone:.2f}")
print(f"{bus_percnt:.2f}%")
print(f"{truck_percnt:.2f}%")
print(f"{train_percnt:.2f}%")

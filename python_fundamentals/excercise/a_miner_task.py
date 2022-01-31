command = input()
resources = {}

while command != "stop":
    quantity = int(input())

    if command not in resources:
        resources[command] = 0
    resources[command] += quantity

    command = input()

for key, value in resources.items():
    print(f"{key} -> {value}")


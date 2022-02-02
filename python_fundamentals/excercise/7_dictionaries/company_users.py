command = input().split("->")
companys_info = {}

while command[0] != "End":

    company = command[0]
    employee = command[1]

    if company not in companys_info:
        companys_info[company] = []
        companys_info[company].append(employee)

    elif employee not in companys_info[company]:
        companys_info[company].append(employee)

    command = input().split("->")

for key in companys_info.keys():
    print(key)
    for index in range(len(companys_info[key])):
        print(f"--{companys_info[key][index]}")


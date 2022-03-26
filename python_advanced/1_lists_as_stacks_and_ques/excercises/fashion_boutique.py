clothes = [int(x) for x in input().split()]
rack_capacy = int(input())
temp_rack = 0
rack_counter = 1

while clothes:
    temp_cloth = clothes.pop()

    if temp_cloth + temp_rack == rack_capacy:
        rack_counter += 1
        temp_rack = 0
    elif temp_cloth + temp_rack > rack_capacy:
        rack_counter += 1
        temp_rack = temp_cloth
    else:
        temp_rack += temp_cloth

print(rack_counter)
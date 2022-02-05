items = input().split()
resources = {"shards": 0, "fragments": 0, "motes": 0}
junk_resources = {}
legendary_item = ""

while legendary_item == "":

    for index in range(0, len(items), 2):
        key = items[index + 1].lower()
        value = int(items[index])
        if key in resources:
            resources[key] += value
        elif key not in junk_resources:
            junk_resources[key] = value
        else:
            junk_resources[key] += value

        if resources["shards"] >= 250:
            resources["shards"] -= 250
            legendary_item = "Shadowmourne"
            print("Shadowmourne obtained!")
            break
        elif resources["fragments"] >= 250:
            resources["fragments"] -= 250
            legendary_item = "Valanyr"
            print("Valanyr obtained!")
            break
        elif resources["motes"] >= 250:
            resources["motes"] -= 250
            legendary_item = "Dragonwrath"
            print("Dragonwrath obtained!")
            break
    if legendary_item != "":
        break
    items = input().split()

for key, value in resources.items():
    print(f"{key}: {value}")
for key, value in junk_resources.items():
    print(f"{key}: {value}")
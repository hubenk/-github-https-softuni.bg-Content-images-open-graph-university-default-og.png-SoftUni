characters = input().split(", ")

dict_comprehention = {element: ord(element) for element in characters}

print(dict_comprehention)
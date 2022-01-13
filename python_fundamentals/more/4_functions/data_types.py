def data_types(type, num_str):
    if type == "int":
        result = int(num_str) * 2
    elif type == "real":
        result = f"{(float(num_str) * 1.5):.2f}"
    elif type == "string":
        result = f"${num_str}$"

    return result


type_input = input()
type_num_str = input()

print(data_types(type_input, type_num_str))

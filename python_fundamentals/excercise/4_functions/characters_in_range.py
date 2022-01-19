def single_string(start, end):
    final_string = ""
    for symbol in range(ord(start) + 1, ord(end)):
        final_string += chr(symbol) + " "

    return final_string


string1 = input()
string2 = input()

print(single_string(string1, string2))

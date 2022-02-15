core_word = input()
core_string = input()

while core_word in core_string:
    core_string = core_string.replace(core_word, "")

print(core_string)
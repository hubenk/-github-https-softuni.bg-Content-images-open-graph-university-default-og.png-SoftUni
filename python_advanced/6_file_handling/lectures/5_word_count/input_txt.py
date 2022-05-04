def input_txt(text):
    with open("input.txt", "w") as file:
        file.write(text)


input_txt("-I was quick to judge him, but it wasn't his fault."
          "\n-Is this some kind of joke?! Is it?"
          "\n-Quick, hide here...It is safer.")

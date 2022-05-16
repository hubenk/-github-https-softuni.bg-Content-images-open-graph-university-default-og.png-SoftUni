def write_text(text):
    with open("text.txt", "w") as file:
        file.writelines(text)


write_text("-I was quick to judge him, but it wasn't his fault."
           "\n-Is this some kind of joke?! Is it?"
           "\n-Quick, hide here. It is safer.")

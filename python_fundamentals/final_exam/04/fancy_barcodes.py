import re

barcodes = int(input())
regex = r"([@][#]+)[A-Z][A-Za-z0-9]{4,}[A-Z](\1)"


for code in range(barcodes):
    valid_barcode = False
    sequence = input()
    checking = re.finditer(regex, sequence)
    digits = ""
    for el in checking:
        valid_barcode = True
        to_check = el.group()
        for char in to_check:
            if char.isdigit():
                digits += char

    if valid_barcode:
        if digits == "":
            print("Product group: 00")
        else:
            print(f"Product group: {digits}")
    else:
        print("Invalid barcode")

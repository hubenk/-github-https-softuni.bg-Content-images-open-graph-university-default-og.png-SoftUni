x = float(input())
y = float(input())
h = float(input())

stranichni_steni = (x * y - 1.5 * 1.5) * 2
zadna_stena = x * x
predna_stena = x * x - 1.2 * 2

pravoyylnik_pokriv = (x * y) * 2
triygylnik_pokriv = (x * h / 2) * 2

tottal_green = stranichni_steni + zadna_stena + predna_stena
tottal_red = pravoyylnik_pokriv + triygylnik_pokriv

green_paint = tottal_green / 3.4
red_paint = tottal_red / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
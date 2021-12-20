movie = input()
days = int(input())
tickets = int(input())
price_for_ticket = float(input())
cinema_cut = 1 - (int(input()) / 100)

gross_income = days * tickets * price_for_ticket
net_income = gross_income * cinema_cut

print(f"The profit from the movie {movie} is {net_income:.2f} lv.")
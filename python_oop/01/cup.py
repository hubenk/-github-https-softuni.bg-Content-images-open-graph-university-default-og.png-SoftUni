class Cup:
    __free_space = 0

    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, amount: int):
        Cup.__free_space = self.quantity + amount
        if Cup.__free_space < self.size:
            self.quantity += amount

    def status(self):
        Cup.__free_space = self.size - self.quantity
        return Cup.__free_space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

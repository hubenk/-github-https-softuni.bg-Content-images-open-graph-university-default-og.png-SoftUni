from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOOD = ["Vegetable", "Fruit"]
    WEIGHT_MULTIPLIER = 0.10

    def __init__(self, name, weight, living_region):
        super(Mouse, self).__init__(name, weight, living_region)

    def make_sound(self):
        return "Sqeak"


class Dog(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_MULTIPLIER = 0.40

    def __init__(self, name, weight, living_region):
        super(Dog, self).__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOOD = ["Vegetable", "Meat"]
    WEIGHT_MULTIPLIER = 0.30

    def __init__(self, name, weight, living_region):
        super(Cat, self).__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_MULTIPLIER = 1.00

    def __init__(self, name, weight, living_region):
        super(Tiger, self).__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"


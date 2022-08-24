from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_MULTIPLIER = 0.25

    def __init__(self, name, weight, wing_size):
        super(Owl, self).__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOOD = ["Vegetable", "Fruit", "Meat", "Seed"]
    WEIGHT_MULTIPLIER = 0.35

    def __init__(self, name, weight, wing_size):
        super(Hen, self).__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

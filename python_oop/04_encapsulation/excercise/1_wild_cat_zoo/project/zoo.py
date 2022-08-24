class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return f"Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return f"Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animal_expenses = 0
        for animal in self.animals:
            animal_expenses += animal.money_for_care

        if self.__budget < animal_expenses:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= animal_expenses
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)

        result = f"You have {len(self.animals)} animals\n"

        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion.__repr__()}\n"

        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger.__repr__()}\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah.__repr__()}\n"

        return result.strip()

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper.__repr__()}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker.__repr__()}\n"

        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += f"{vet.__repr__()}\n"

        return result.strip()

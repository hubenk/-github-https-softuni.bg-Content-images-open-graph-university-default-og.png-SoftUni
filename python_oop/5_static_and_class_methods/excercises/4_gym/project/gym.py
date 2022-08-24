from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.equipment = []
        self.subscriptions = []
        self.trainers = []
        self.plans = []

    @staticmethod
    def result_print(object, id):
        for x in object:
            if x.id == id:
                result = x
                return result

    def add_customer(self, customer: Customer):
        for custom in self.customers:
            if custom.name == customer.name:
                return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        for train in self.trainers:
            if train.name == trainer.name:
                return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        for equip in self.equipment:
            if equip.name == equipment.name:
                return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        for explan in self.plans:
            if explan.id == plan.id:
                return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        for sub in self.subscriptions:
            if sub.id == subscription.id:
                return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result_sub = f"{Gym.result_print(self.subscriptions, subscription_id)}"
        result_cust = f"{Gym.result_print(self.customers, subscription_id)}"
        result_train = f"{Gym.result_print(self.trainers, subscription_id)}"
        result_equip = f"{Gym.result_print(self.equipment, subscription_id)}"
        result_plan = f"{Gym.result_print(self.plans, subscription_id)}"
        return repr(result_sub) + "\n" + repr(result_cust) + "\n" + repr(result_train) + "\n" + repr(result_equip) + \
            "\n" + repr(result_plan)


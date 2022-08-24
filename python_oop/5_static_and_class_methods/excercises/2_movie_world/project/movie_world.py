from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = ""
        dvd = ""
        for x in self.customers:
            if x.id == customer_id:
                customer = x

        for y in self.dvds:
            if y.id == dvd_id:
                dvd = y

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        if dvd.is_rented:
            return "DVD is already rented"

        if len(customer.rented_dvds) == 0:
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

        for x in customer.rented_dvds():
            if x.name == dvd.name:
                return f"{customer.name} has already rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = ""
        dvd = ""

        for x in self.customers:
            if x.id == customer_id:
                customer = x
        for y in self.dvds:
            if y.id == dvd_id:
                dvd = y

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return "\n".join([repr(x) for x in self.customers]) + \
               "\n" + \
               "\n".join([str(x) for x in self.dvds])



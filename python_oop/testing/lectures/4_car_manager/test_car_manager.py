import unittest

from car_manager import Car

class CarTest(unittest.TestCase):
    make = "make"
    model = "model"
    fuel_consumption = 10
    fuel_capacity = 100

    def test_make_setter__when_none_entry__raise_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            car.make = None
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter__when_none_entry_raise_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            car.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_sonsumption__when_zero__raise_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity__when_zero__raise_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount__when_negative_amount__raise_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel__when_fuel_is_negative_raise_error(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            car.refuel(-2)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel__when_fuel_is_zero_raise_error(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel__when__fuel_is_positive_and_amount_less_than_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount = 50
        fuel = 10

        car.refuel(fuel)

        self.assertEqual(60, car.fuel_amount)

    def test_refuel__when__fuel_is_positive_and_amount_more_than_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount = 50
        fuel = 60

        car.refuel(fuel)

        self.assertEqual(car.fuel_capacity, car.fuel_amount)

    def test_drive_when_needed_fuel_is_more_than_fuel_amount_raise_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount = 100

        with self.assertRaises(Exception) as ex:
            car.drive(99999)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_when_needed_fuel_is_less_than_fuel_amount(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount = 100

        car.drive(200)

        self.assertEqual(80, car.fuel_amount)


if __name__ == '__main__':
    unittest.main()
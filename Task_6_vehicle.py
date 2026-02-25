class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate  # base rate per day

    def calculate_rental(self, days):
        # This method will be overridden by subclasses
        return self.rental_rate * days


# Subclass: Car
class Car(Vehicle):
    def __init__(self, model, rental_rate, seats):
        super().__init__(model, rental_rate)
        self.seats = seats

    def calculate_rental(self, days):
        # Cars have a fixed daily rate
        return self.rental_rate * days


# Subclass: Bike
class Bike(Vehicle):
    def __init__(self, model, rental_rate, bike_type):
        super().__init__(model, rental_rate)
        self.bike_type = bike_type

    def calculate_rental(self, days):
        # Bikes get a 10% discount for rentals over 5 days
        total = self.rental_rate * days
        if days > 5:
            total *= 0.9
        return total


# Subclass: Truck
class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity  # in tons

    def calculate_rental(self, days):
        # Trucks charge extra based on load capacity
        extra_charge = self.load_capacity * 50
        return (self.rental_rate + extra_charge) * days


# Polymorphism in action
vehicles = [
    Car("Toyota Corolla", 50, 5),
    Bike("Yamaha R15", 20, "Sports"),
    Truck("Volvo FH", 100, 10)
]

days = 7

for vehicle in vehicles:
    print(f"{vehicle.model} rental cost for {days} days: ${vehicle.calculate_rental(days)}")
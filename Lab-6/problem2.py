# Parent class
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    # Method to calculate normal fare
    def fare(self):
        return self.seating_capacity * 100


# Child class
class Bus(Vehicle):

    # Override the fare() method
    def fare(self):
        normal_fare = super().fare()      # Get fare from Vehicle class
        maintenance_charge = normal_fare * 0.10   # 10% extra
        total_fare = normal_fare + maintenance_charge
        return total_fare


# Create a Bus object
bus = Bus(50)

# Display the total fare
print("Bus Seating Capacity:", bus.seating_capacity)
print("Total Bus Fare:", bus.fare())
# Part 1:
    # Assumption:
        # All students get 10% off
        # All students are regular buyers
        # Regular buyers all get 5% off
def student_discount(x):
    # Student discount always gets buyer discount. Calculate student discount then buyer discount off of that rate.
    return regular_buyer_discount(x * 0.9)

def regular_buyer_discount(x):
    return x * 0.95

print(student_discount(100))
print(regular_buyer_discount(100))

# Part 2:
result = (lambda x: x * (x+5) **2)(5)
print(result)

# Part 3:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def discount_products_10_percent(x):
    return x * 0.9
result = list(map(discount_products_10_percent, my_list))
print(result)

# Part 4:
class computer:
    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def get_specs(self):
        return {self.processor, self.ram, self.storage}
    def display_specs(self):
        print("--------------------------------")
        print("Processor: " + self.processor)
        print("Ram: " + self.ram)
        print("Storage: " + self.storage)

class desktop(computer):
    def __init__(self, processor, ram, storage, power_supply):
        super().__init__(processor, ram, storage)
        self.power_supply = power_supply

    def get_specs(self):
        specs = super().get_specs().copy()
        specs.update({self.power_supply})
        return specs

    def display_specs(self):
        super().display_specs()
        print("Power Supply: " + self.power_supply)
class laptop(computer):
    def __init__(self, processor, ram, storage, weight):
        super().__init__(processor, ram, storage)
        self.weight = weight

    def get_specs(self):
        specs = super().get_specs().copy()
        specs.update({self.weight})
        return specs

    def display_specs(self):
        super().display_specs()
        print("Weight: " + self.weight)


computer = computer("Intel Core i9-11900K", "16GB", "500GB")
desktop = desktop("Qualcomm Snapdragon 8cx Gen 3", "32GB", "2TB", "Corsair RM850x")
laptop = laptop("AMD Ryzen 9 5950X", "8GB", "1TB", "2.01KG")

computer.display_specs()
desktop.display_specs()
laptop.display_specs()
print(computer.get_specs())
print(desktop.get_specs())
print(laptop.get_specs())

# Part 5:
class operator_overloading:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value + other

value = operator_overloading(10)

print(value * 10)

# class Car:
class Car:
    # Class attributes / Default values
    oil_qty = 0
    tires = 4
    name = ''

    def __init__(self, name, oil_qty, tires):
        self.name = name
        self.oil_qty = oil_qty
        self.tires = tires

    def run(self):
        print(self.name + ' is running!!!')

    def stopped(self):
        print('im stopped!!!')

    def refill(self, fuel_qty):
        self.oil_qty += fuel_qty
        print('fuel quty now ' + str(self.oil_qty))


# Object instantiation
car_maruti = Car('maruti', 10, 4)
car_hyundai = Car('hyundai', 20, 4)

# # shallow copy, deep copy
car_hyundai.name = "buggati"

# Printing attributes for car_maruti
print(car_maruti.name)
print(car_maruti.oil_qty)
print(car_maruti.tires)

# Printing attributes for car_hyundai
print(car_hyundai.name)
print(car_hyundai.oil_qty)
print(car_hyundai.tires)

# Calling instance methods
car_hyundai.run()
car_hyundai.stopped()
car_hyundai.refill(20)
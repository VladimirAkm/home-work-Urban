class House:

    def __init__(self):
        self.numberOfFloors = 10
        print("Текущий этаж равен", self.numberOfFloors)


house = House()

house.numberOfFloors = 1

while house.numberOfFloors < 10:
    house.numberOfFloors += 1
print("Текущий этаж равен", house.numberOfFloors)

class House:

    def __init__(self):
        self.floors = None
        self.numberOfFloors = 0

    def new_numberOfFloors(self, floors):
        self.floors = floors


House1 = House()
for floors in range(0, 10):
    House1.new_numberOfFloors = House1.numberOfFloors + floors
    print('Текущий этаж House1 равен:', House1.new_numberOfFloors + 1)

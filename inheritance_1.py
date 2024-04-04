class Car:
    Price = 1000000

    def horse_powers(self):
        self.horse_powers = 0

    def __str__(self):
        return '{}: стоимость- {}, мощность- {} '.format(self.__class__.__name__, self.Price, self.horse_powers)


class Nissan(Car):
    Price = 1500000
    def horse_powers(self):
        self.horse_powers = 2000


class Kia(Car):
    Price = 1200000
    def horse_powers(self):
        self.horse_powers = 1600


nissan = Nissan()
nissan.horse_powers()
print(nissan)

kia = Kia()
kia.horse_powers()
print(kia)

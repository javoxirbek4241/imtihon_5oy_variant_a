# 3.Mashina ro‘yxati
# Car(brand, model, year, mileage) nomli namedtuple.
# Foydalanuvchi 5 ta mashina kiritadi. Eng kam yurgan mashinani toping.

from collections import namedtuple

Car = namedtuple("Car", ('brand', 'model', 'year', 'millage'))
c1 = Car('gm', 'malibu', 2020, 10700)
c2 = Car('gm', 'gentra', 2022, 2000)
c3 = Car('gm', 'cobalt', 2018, 39200)
c4 = Car('gm', 'nexiya', 2019, 3000)
c5 = Car('gm', 'cobalt', 2015, 39200)

cars = [c1, c2, c3, c4, c5]
print((min(i.millage for i in cars)))



















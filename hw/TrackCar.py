from time import sleep


class Auto:
    def __init__(self, brand, age, mark, color='Black', weight='2t', ):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("Move")

    def stop(self):
        print('Stop')

    def birthday(self):
        self.age += 1
        print(self.age)


class Truck(Auto):
    def __init__(self,max_load, brand, age, mark, color='Black', weight='2t', ):
        super().__init__(brand, age, mark, color='Black', weight='2t', )
        self.max_load = max_load

    def load(self):
        sleep(1)
        print('Load')
        sleep(1)

    def move(self):
        return print('Attention'), super().move()


class Car(Auto):
    def __init__(self, max_speed, brand, age, mark, color='Black', weight='2t'):
        super().__init__(brand, age, mark, color, weight)
        self.maxspeed = max_speed

    def max_speed(self):
        print(f'Max speed is {self.maxspeed}')


t = Truck('500 litres','Mersedes', 20, 'Actros', color='white', weight='18t')
t.move()
t.stop()
t.load()
t.birthday()
print(t.__dict__)
c = Car('220 km/h', 'Bmw', 22, 'e38')
c.move()
c.stop()
c.birthday()
c.max_speed()
print(c.__dict__)

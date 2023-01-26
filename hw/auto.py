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


a = Auto('Bmw', 22, 'e38')

a.move()
a.stop()
a.birthday()
a.birthday()
print(a.__dict__)

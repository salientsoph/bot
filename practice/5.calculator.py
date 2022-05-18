

class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plus(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def multiple(self):
        return self.x * self.y

    def devide(self):
        return self.x / self.y


cal1 = calculator(1, 2)
print(cal1.devide())
print(cal1.multiple())
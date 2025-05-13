x = 5

print(type(x))
print(dir(x))
print(x.numerator)
print(x.denominator)

class MyClass:
    total = 6

    def say_hello():
        print("Hello")

print(MyClass.total)
MyClass.say_hello()

obj = MyClass()
print(obj)
print(dir(obj))


import math

class Fraction:
    def __init__(self, num, denom): #constructor
        self.numerator = num
        self.denominator = denom

    def __str__(self): # double underscore dunder/magic method
        return "{} / {}".format(self.numerator, self.denominator)

    def simplify(self):
        g = math.gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

    def add(self, f):
        denom = math.lcm(self.denominator, f.denominator)
        num = (denom // self.denominator) * self.numerator + \
              (denom // f.denominator) * f.numerator
        self.numerator = num
        self.denominator = denom

    def __str__(self): # double underscore dunder/magic method
        return "{} / {}".format(self.numerator, self.denominator)

    def __add__(self, f):
        denom = math.lcm(self.denominator, f.denominator)
        num = (denom // self.denominator) * self.numerator + \
              (denom // f.denominator) * f.numerator
        return Fraction(num, denom)

f1 = Fraction(20, 40)
f2 = Fraction(30, 60)
print(f1.numerator, f1.denominator)
print(f1)

f1.simplify()
print(f1)

f1.add(f2)
print(f1)

f3 = f1 + f2
print(f3)
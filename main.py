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

class Fraction:
    def __init__(self, num, denom): #constructor
        self.numerator = num
        self.denominator = denom
        print("init")

f1 = Fraction(20, 40)
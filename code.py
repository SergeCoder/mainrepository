from math import pi
import re

class Apple:
    """получает данные о яблоки"""
    def __init__(self, weight, color, volume, taste):
        self.weight = weight
        self.color = color
        self.volume = volume
        self.taste = taste

apple = Apple(10, "red", 30, "delicious")

class Circle:
    """получает радиус"""
    def __init__(self, r):
        self.radius = r

    def count_area(self):
        """считает площадь"""
        return pi * self.radius**2

circle = Circle(16)

class Triangle:
    """получает длину стороны и высоту"""
    def __init__(self, s, h):
        self.side = s
        self.height = h

    def area(self):
        """считает площадь"""
        return self.side * self.height / 2

triangle = Triangle(10, 5)

class Hexagon:
    """получает длины шести сторон"""
    def __init__(self, f, s, t, fo, fi, si):
        self.first = f
        self.second = s
        self.third = t
        self.fourth = fo
        self.fifth = fi
        self.sixth = si

    def count_perimeter(self):
        """считает периметр"""
        return self.first + self.second + self.third + self.fourth + self.fifth + self.sixth

hexagon = Hexagon(1, 3, 5, 7, 9, 11)

class Shape:
    def what_am_i(self):
        return 'Я - фигура.'

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.length)
        return perimeter

class Square(Shape):
    square_list = []
    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    def __repr__(self):
        return (f'{self.side} на {self.side} '
                f'на {self.side} на {self.side}')

    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def change_size(self, num):
        self.side = self.side + num

rec = Rectangle(10, 15)
rec.calculate_perimeter()

sq = Square(10)
sq1 = Square(11)
sq.change_size(5)

class Horse:
    def __init__(self, name, owner, color):
        self.name = name
        self.owner = owner
        self.color = color

class Person:
    def __init__(self, name, win):
        self.name = name
        self.win = win

mike = Person('Майку', 5)
horse = Horse('Макс', mike, 'черного')

def are_objects_same(first, second):
    return True if first is second else False

with open('zen.txt', 'r') as f:
    file = f.read()
    word = re.findall('Dutch', file)

city1 = 'Москва: 777, 999, 797.'
city2 = 'Тула: 071, 950, 112.'

num1 = re.findall('\\d', city1)
num2 = re.findall('\\d', city2)


text = 'Привидение прошуршало и исчезло в углу'
matches = re.findall('.ло', text)
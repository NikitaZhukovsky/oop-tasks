import math


class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_info(self):
        return self.radius, self.x, self.y, self.z

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return volume

    def get_square(self):
        area = 4 * math.pi * (self.radius ** 2)
        return area

    def get_radius(self):
        return self.radius

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_radius(self, radius):
        self.radius = radius


sphere = Sphere(5, 1, 2, 3)
print(f"Параметры сферы: {sphere.get_info()}")
print(f"Объем шара ограниченной текущей сферой: {sphere.get_volume()}")
print(f"Площадь внешней поверхности сферы: {sphere.get_square()}")
print(f"Радиус текущей сферы: {sphere.get_radius()}")
print(f"Центр сферы: {sphere.get_center()}")

sphere.set_radius(10)
print(f"Сфера с новым радиусом: {sphere.get_radius()}")

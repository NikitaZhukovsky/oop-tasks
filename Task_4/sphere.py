import math


class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        if all(isinstance(coord, (int, float)) for coord in (x, y, z)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError("Координаты должны быть числами.")

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return volume

    def get_square(self):
        area = 4 * math.pi * (self.radius ** 2)
        return area

    def get_radius(self):
        if isinstance(self.radius, (int, float)) and self.radius > 0:
            return self.radius
        else:
            raise ValueError("Радиус должен быть положительным числом.")

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, radius):
        if isinstance(radius, (int, float)) and radius > 0:
            self.radius = radius
        else:
            raise ValueError("Радиус должен быть положительным числом.")

    def set_center(self, x, y, z):
        if all(isinstance(coord, (int, float)) for coord in (x, y, z)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError("Координаты должны быть числами.")

    def is_point_inside(self, x, y, z):
        if all(isinstance(coord, (int, float)) for coord in (x, y, z)):
            distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2)
            return True if distance <= self.radius else False
        else:
            raise ValueError("Координаты точки должны быть числами.")


sphere = Sphere(10)
print(f"Параметры сферы: радиус - {sphere.get_radius()}, центр - {sphere.get_center()}")
print(f"Объем шара, ограниченного текущей сферой: {sphere.get_volume()}")
print(f"Площадь внешней поверхности сферы: {sphere.get_square()}")

sphere.set_radius(-10)
sphere.set_center(2, 3, 4)
print(f"Новые параметры сферы: радиус - {sphere.get_radius()}, центр - {sphere.get_center()}")

print(f"Точка находится внутри сферы: {sphere.is_point_inside(5, 6, 8)}")

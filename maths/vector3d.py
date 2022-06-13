import math


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, vec):
        return Vector3D(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __sub__(self, vec):
        return Vector3D(self.x - vec.x, self.y - vec.y, self.z - vec.z)

    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def __mul__(self, num):
        return Vector3D(self.x * num, self.y * num, self.z * num)

    def __truediv__(self, num):
        return Vector3D(self.x / num, self.y / num, self.z / num)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalize(self):
        return self / self.length()

    def reflect(self, vec):
        return (
            self * Vector3D.dot(self, vec) / Vector3D.dot(self, self) * 2 - vec
        ).normalize()

    def dot(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z

    def cross(a, b):
        return Vector3D(
            a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x
        )

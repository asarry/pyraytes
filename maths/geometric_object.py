from maths.vector3d import Vector3D
import math


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction


class Plane:
    def __init__(self, normal, intercept):
        self.normal = normal
        self.intercept = intercept

    def intersection(self, ray):
        div = Vector3D.dot(ray.direction, self.normal)
        if div == 0:  # Plane and ray are parallel!
            return None
        t = -(Vector3D.dot(ray.origin, self.normal) + self.intercept) / div
        if t > 0:
            return t
        else:
            return None


class Sphere:
    def __init__(self, position, radius):
        self.position = position
        self.radius = radius

    def intersection(self, ray):
        tca = Vector3D.dot(self.position - ray.origin, ray.direction)
        if tca < 0:
            return None
        d2 = (
            Vector3D.dot(self.position - ray.origin, self.position - ray.origin)
            - tca * tca
        )
        if d2 > self.radius**2:
            return None
        thc = math.sqrt(self.radius**2 - d2)
        ret = min(tca - thc, tca + thc)
        if ret < 0:
            return None
        else:
            return ret


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

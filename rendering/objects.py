from rendering.color import Color
from rendering.material import Material
from maths.vector3d import Vector3D
import math


class Object:
    def __init__(self, material):
        self.material = material

    def intersection(self, ray):
        """Considering intersection point is: landa * ray, returns landa if there is intersection or None"""
        pass

    def normal_at(self, position):
        """Returns normal vector of this shape on a position"""
        pass

    def color_at(self, position):
        pass


class Plane(Object):
    def __init__(self, material, normal, intercept):
        super().__init__(material)
        self.normal = normal
        self.intercept = intercept

    def intersection(self, ray):
        dot_res = Vector3D.dot(ray.direction, self.normal)
        if dot_res == 0:
            return None
        dist = -(Vector3D.dot(ray.origin, self.normal) + self.intercept) / dot_res
        if dist > 0:
            return dist
        else:
            return None

    def normal_at(self, position):
        return self.normal

    def color_at(self, position):
        return self.material.color_at(position)


class Sphere(Object):
    def __init__(self, material, position, radius):
        super().__init__(material)
        self.position = position
        self.radius = radius

    def intersection(self, ray):
        dist_to_ray = ray.origin - self.position
        b = 2 * Vector3D.dot(dist_to_ray, ray.direction)
        c = Vector3D.dot(dist_to_ray, dist_to_ray) - self.radius**2
        delta = b**2 - 4 * c

        if delta >= 0:
            dist = (-b - math.sqrt(delta)) / 2
            if dist > 0:
                return dist
        return None

    def normal_at(self, position):
        return (position - self.position).normalize()

    def color_at(self, position):
        return self.material.color

from maths.vector3d import Vector3D
from rendering.color import Color
from rendering.material import Material
import math


class Object:
    """An Object has a material attached to it and must implement an intersect method, a normal_at method and a color_at method."""

    def __init__(self, material):
        self.material = material

    def intersect(self, ray):
        """Returns the distance to the intersection if there is one and None otherwise."""
        pass

    def normal_at(self, position):
        """Returns the normal vector of this object at a given position."""
        pass

    def color_at(self, position):
        """Returns the color of this object at a given position."""
        pass


class Plane(Object):
    """A Plane has a normal and an intercept."""

    def __init__(self, material, normal, intercept):
        super().__init__(material)
        self.normal = normal
        self.intercept = intercept

    def intersect(self, ray):
        """Returns the distance to the intersection if there is one and None otherwise."""
        dot_res = Vector3D.dot(ray.direction, self.normal)
        if dot_res == 0:
            return None
        dist = -(Vector3D.dot(ray.origin, self.normal) + self.intercept) / dot_res
        if dist > 0:
            return dist
        else:
            return None

    def normal_at(self, position):
        """Returns the normal vector of this object at a given position."""
        return self.normal

    def color_at(self, position):
        """Returns the color of this object at a given position."""
        return self.material.color_at(position)


class Sphere(Object):
    """A Sphere has a position and a radius."""

    def __init__(self, material, position, radius):
        super().__init__(material)
        self.position = position
        self.radius = radius

    def intersect(self, ray):
        """Returns the distance to the intersection if there is one and None otherwise."""
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
        """Returns the normal vector of this object at a given position."""
        return (position - self.position).normalize()

    def color_at(self, position):
        """Returns the color of this object at a given position."""
        return self.material.color

from rendering.color import Color
from rendering.material import Material
from maths import geometric_object
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
        self.math_repr = geometric_object.Plane(normal, intercept)

    def intersection(self, ray):
        return self.math_repr.intersection(ray)

    def normal_at(self, position):
        return self.math_repr.normal

    def color_at(self, position):
        return self.material.color


class CheckerboardUpPlane(Plane):
    def __init__(self, material, intercept, cell_size, cell_color):
        super().__init__(material, Vector3D(0, 1, 0), intercept)
        self.cell_size = cell_size
        self.cell_color = cell_color

    def color_at(self, position):
        checker = math.floor(position.x / self.cell_size) + math.floor(
            position.z / self.cell_size
        )
        if checker % 2 == 0:
            return self.material.color
        else:
            return self.cell_color


class Sphere(Object):
    def __init__(self, material, position, radius):
        super().__init__(material)
        self.math_repr = geometric_object.Sphere(position, radius)

    def intersection(self, ray):
        return self.math_repr.intersection(ray)

    def normal_at(self, position):
        return (position - self.math_repr.position).normalize()

    def color_at(self, position):
        return self.material.color

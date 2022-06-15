from maths.vector3d import Vector3D
from rendering.ray import Ray
import math


class Camera:
    def __init__(self, position, direction, up, aspect_ratio, fov=math.pi / 4):
        self.position = position
        self.direction = direction
        self.up = up
        self.aspect_ratio = aspect_ratio
        self.fov = fov

        self._height = math.tan(self.fov / 2) * 2
        self._width = self.aspect_ratio * self._height

        self._right = Vector3D.cross(self.up, self.direction).normalize()
        self._up = Vector3D.cross(self.direction, self._right).normalize()

    def corresponding_ray(self, image_size, pixel_index):
        pixel_pos = (
            self.direction
            + self._right * self._width * (pixel_index[0] / image_size[0] - 0.5)
            + self._up * self._height * (pixel_index[1] / image_size[1] - 0.5)
        )

        return Ray(self.position, (pixel_pos).normalize())

    def create_lookat(position, target, up, aspect_ratio, fov=math.pi / 4):
        return Camera(position, (target - position).normalize(), up, aspect_ratio, fov)

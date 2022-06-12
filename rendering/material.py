from rendering.color import Color
import math


class Material:
    def __init__(
        self, color, diffuse_rate, specular_rate, specular_exponent, reflection_rate
    ):
        self.color = color
        self.diffuse_rate = diffuse_rate
        self.specular_rate = specular_rate
        self.specular_exponent = specular_exponent
        self.reflection_rate = reflection_rate

    def color_at(self, position):
        return self.color


class CheckeredMaterial(Material):
    def __init__(
        self,
        prim_color,
        sec_color,
        diffuse_rate,
        specular_rate,
        specular_exponent,
        reflection_rate,
        cell_size,
    ):
        super().__init__(
            prim_color, diffuse_rate, specular_rate, specular_exponent, reflection_rate
        )
        self.sec_color = sec_color
        self.cell_size = cell_size

    def color_at(self, position):
        if (
            math.floor(position.x / self.cell_size)
            + math.floor(position.z / self.cell_size)
        ) % 2 == 0:
            return self.color
        else:
            return self.sec_color

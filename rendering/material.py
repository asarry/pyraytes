from rendering.color import Color
import math


class Material:
    """A Material has multiple properties such as a color, a diffuse rate, a specular rate, a specular exponent and a reflection rate. It defines a color_at method as well."""

    def __init__(
        self, color, diffuse_rate, specular_rate, specular_exponent, reflection_rate
    ):
        self.color = color
        self.diffuse_rate = diffuse_rate
        self.specular_rate = specular_rate
        self.specular_exponent = specular_exponent
        self.reflection_rate = reflection_rate

    def color_at(self, position):
        """Returns the color of this material at a given position."""
        return self.color


class CheckeredMaterial(Material):
    """A CheckeredMaterial inherits from the Material class and requires a secondary color as well as a cell size."""

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
        """Returns the color of this material at a given position."""
        if (
            math.floor(position.x / self.cell_size)
            + math.floor(position.z / self.cell_size)
        ) % 2 == 0:
            return self.color
        else:
            return self.sec_color

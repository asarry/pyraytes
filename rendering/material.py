from rendering.color import Color


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
    ):
        super().__init__(
            prim_color, diffuse_rate, specular_rate, specular_exponent, reflection_rate
        )
        self.sec_color = sec_color

    def color_at(self, position):
        if True:
            return self.color
        else:
            return sec_color

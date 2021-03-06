class Color:
    """A Color is defined by its red, green and blue components."""

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_bytes(self):
        """Returns the color in the byte format."""
        return bytes(
            [
                int(min(self.r * 255, 255)),
                int(min(self.g * 255, 255)),
                int(min(self.b * 255, 255)),
            ]
        )

    def __add__(self, color):
        return Color(self.r + color.r, self.g + color.g, self.b + color.b)

    def __sub__(self, color):
        return Color(self.r - color.r, self.g - color.g, self.b - color.b)

    def __mul__(self, other):
        if isinstance(other, Color):
            return Color(self.r * other.r, self.g * other.g, self.b * other.b)
        else:
            return Color(self.r * other, self.g * other, self.b * other)

    def __truediv__(self, other):
        if isinstance(other, Color):
            return Color(self.r / other.r, self.g / other.g, self.b / other.b)
        else:
            return Color(self.r / other, self.g / other, self.b / other)

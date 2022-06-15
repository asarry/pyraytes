import io


class Image:
    """An Image has a width, a height, an initial color and can be saved in specific formats."""

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.data = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(color)
            self.data.append(row)

    def save_as_ppm(self, name):
        """Save the image with the given name in the PPM format."""
        with io.open(name, mode="wb") as file:
            file.write(bytes(f"P6 {self.width} {self.height} 255\n", "ascii"))
            for row in reversed(self.data):
                for color in row:
                    file.write(color.get_bytes())

import io


class Image:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.data = []
        for h in range(height):
            row = []
            for w in range(width):
                row.append(color)
            self.data.append(row)

    def clear(self, color):
        for h in range(self.height):
            for w in range(self.width):
                self.data[h][w] = color

    def save_as_ppm(self, name, image):
        with io.open(name, mode="wb") as file:
            file.write(bytes(f"P6 {image.width} {image.height} 255\n", "ascii"))
            for row in reversed(image.data):
                for color in row:
                    file.write(color.get_bytes())

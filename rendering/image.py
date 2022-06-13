import io


class Image:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.data = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(color)
            self.data.append(row)

    def clear(self, color):
        for i in range(self.height):
            for j in range(self.width):
                self.data[i][j] = color

    def save_as_ppm(self, name, image):
        with io.open(name, mode="wb") as file:
            file.write(bytes(f"P6 {image.width} {image.height} 255\n", "ascii"))
            for row in reversed(image.data):
                for color in row:
                    file.write(color.get_bytes())

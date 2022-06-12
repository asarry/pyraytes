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

    def save_ppm(self, name, frame):
        with io.open(name, mode="wb") as f:
            f.write(b"P6 ")
            f.write(str(frame.width).encode("ascii"))
            f.write(b" ")
            f.write(str(frame.height).encode("ascii"))
            f.write(b" 255\n")
            for row in reversed(frame.data):
                for color in row:
                    f.write(color.get_bytes())

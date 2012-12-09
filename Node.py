class Node:
    offset = 5

    def __init__(self, x, y, visited=False):
        self.x = x
        self.y = y
        self.color = "black"

        if visited:
            self.color = "green"

    def get_coords(self):
        return [self.x, self.y]

    def compare(self, other):
        if self.get_coords() == other.get_coords():
            return True
        return False

    def draw(self, canvas):
        return canvas.create_oval(self.x - self.offset, self.y - self.offset,
                                  self.x + self.offset, self.y + self.offset,
                                  fill=self.color)

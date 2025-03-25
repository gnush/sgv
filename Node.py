class Node:
    offset = 9

    def __init__(self, x, y, weight=1, visited=False, scale=1):
        self.x = x * scale
        self.y = y * scale
        self.color = "yellow"
        self.weight = weight

        if visited:
            self.color = "green"

    def get_coords(self):
        return [self.x, self.y]

    def compare(self, other):
        if self.get_coords() == other.get_coords():
            return True
        return False

    def draw(self, canvas):
        return [canvas.create_oval(self.x - self.offset, self.y - self.offset,
                                  self.x + self.offset, self.y + self.offset,
                                  fill=self.color),
                canvas.create_text(self.x, self.y, text=self.weight, fill="black")]

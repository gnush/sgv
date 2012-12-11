class Edge:
    width = 2

    def __init__(self, n0, n1, weight = "1", visited=False):
        self.start = n0
        self.end = n1
        self.color = "black"
        self.weight = weight

        if visited:
            self.color = "green"

    def compare(self, other):
        if self.start.compare(other.start) & self.end.compare(other.end):
            return True
        return False

    def draw(self, canvas):
        return [canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=self.color, width=self.width),
                canvas.create_text(min(self.start.x, self.end.x) + abs(self.start.x - self.end.x)/2,
                                   min(self.start.y, self.end.y) + abs(self.start.y - self.end.y)/2,
                                   text=self.weight)]

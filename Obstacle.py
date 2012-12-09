class Obstacle:
    color = "gray"
    stipple = "gray75"

    def __init__(self, xy):
        self.xy = xy

    def draw(self, canvas):
        return canvas.create_polygon(self.xy, stipple=self.stipple, fill=self.color)

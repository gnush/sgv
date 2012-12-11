class Obstacle:
    color = "gray"
    stipple = "gray75"

    def __init__(self, xy, scale=1):
        self.xy = [int(x) * scale for x in xy]

    def text():
        for x in xy:
            print(x)

    def draw(self, canvas):
        return canvas.create_polygon(self.xy, stipple=self.stipple, fill=self.color)

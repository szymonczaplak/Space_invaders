class Bullets:
    def __init__(self):
        self.x = []
        self.y = []
        self.owner = []

    def get_bullet_update(self, list_):
        self.x = list(map(int, list_[0].split()))
        self.y = list(map(int, list_[1].split()))
        self.owner = list(map(int, list_[2].split()))

    def draw(self, pygame, screen):
        for i in range(len(self.x)):
            color = (0, 128, 125)
            if self.owner[i] == "enemy":
                color = (125, 0, 100)
            pygame.draw.lines(screen, color, True, [(self.x[i], self.y[i]),
                                                    (self.x[i], self.y[i] - 5)], 2)

class Bonus:
    def __init__(self, pygame):
        self.x = []
        self.y = []
        self.BONUS = pygame.image.load('bonus.png')

    def get_bonuses_update(self, list_):
        self.x = list(map(int, list_[0].split()))
        self.y = list(map(int, list_[1].split()))

    def draw(self, screen):
        for i in range(len(self.x)):
            screen.blit(self.BONUS, (self.x[i], self.y[i]))

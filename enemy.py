class Enemies:
    def __init__(self, pygame):
        self.x = []
        self.y = []
        self.life = []
        self.weapon = []
        self.ENEMY = pygame.image.load('enemy1.png')
        self.ENEMY_LOW = pygame.image.load('enemy_low.png')

    def get_enemies_update(self, list_):
        self.x = list(map(int, list_[0].split()))
        self.y = list(map(int, list_[1].split()))
        self.life = list(map(int, list_[2].split()))
        self.weapon = list(map(int, list_[3].split()))

    def draw(self, screen):
        for i in range(len(self.x)):
            if self.life[i] > 1:
                screen.blit(self.ENEMY, (self.x[i], self.y[i]))
            if self.life[i] == 1:
                screen.blit(self.ENEMY_LOW, (self.x[i], self.y[i]))

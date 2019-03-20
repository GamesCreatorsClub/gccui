import pygame, sys, time

screen_size = (320, 480)

screen = pygame.display.set_mode(screen_size)

pygame.init()
clock = pygame.time.Clock()

class DotAnimation:
    def __int__(self):
        self.start_time = None
    def start(self):
        self.start_time = time.time()
    def draw(self, surface):
        t = time.time() - self.start_time
        max_y = t if t < 4.8 else 4.79
        up_y = 20
        up_y1 = 50
        pygame.draw.rect(screen, pygame.color.THECOLORS['cyan'], pygame.Rect(5, 5, 310, 470), 1)
        for x in range(30, int(t*120), 20):
            pygame.draw.line(surface, pygame.color.THECOLORS["cyan4"], (x, up_y), (x, up_y1), 2)
            print(up_y, up_y1)
            if x > 270:
                print('x greater than 270')
                up_y = up_y + 40
                up_y1 = up_y1 + 40
                x = x - 240








class LineAnimation:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def draw(self, surface):
        t = time.time() - self.start_time
        max_y = t if t < 4.8 else 4.79

        pygame.draw.rect(screen, pygame.color.THECOLORS['cyan'], pygame.Rect(5, 5, 310, 470), 1)
        for y in range(5, int(t * 150), 20):
            pygame.draw.line(surface, pygame.color.THECOLORS["cyan4"], (5, y), (315, y))
        if t >= 2:
            for x in range(0, int((t-2) * 150), 20):
                pygame.draw.line(surface, pygame.color.THECOLORS["cyan4"], (x, 5), (x, 475))


animation = LineAnimation()
animation1 = DotAnimation()
animation.start()
animation1.start()


while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        animation1.start()

    screen.fill((0, 0, 0))

    animation1.draw(screen)


    pygame.display.flip()
    clock.tick(60)
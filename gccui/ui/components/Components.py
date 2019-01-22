import pygame, time

black = [0, 0, 0]
screen = pygame.display.set_mode((800, 600))
pygame.font.init()
running = True
button_list = {}
font = pygame.font.SysFont('Arial', 30)
class Component:
    def __init__(self, pos):
        self.pos = pos

    def draw(screen):
        pass

class Buttons(Component):
    def __init__(self, x, y, width, height, screen, ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen


    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.height, self.width))

    def grow(self, change_w, change_h):
        self.change_w = change_w
        self.change_h = change_h

        self.width += self.change_w
        self.height += self.change_h

    def render():
        global myObject, myObject4, myObject3, myObject1, myObject2
        myObject = Buttons(320, 280, 80, 150, screen)
        myObject1 = Buttons(myObject.x + 300, myObject.y, 80, 150, screen) #making each button relative to the middle one.
        myObject2 = Buttons(myObject.x, myObject.y + 200, 80, 150, screen) #This doesnt really work, Ill remove it later
        myObject3 = Buttons(myObject.x, myObject.y - 200, 80, 150, screen)
        myObject4 = Buttons(myObject.x - 300, myObject.y, 80, 150, screen)
class objectBorder(Component):
    def __init__(self, object, width):
        self.object object
        self.width = width

    def drawBorder(self, object):
        self.object = object
        

class Label():
    def __init__(self, pos, text, size, colour):
        self.text = text
        self.size = size
        self.colour = colour
        self.pos = pos

    def draw(self, pos, text, size, colour):
        self = font.render(text, colour, size)
        screen.blit(screen, pos)

def expand_click():
    #this is for the onClick() response
    if current_keys[pygame.K_LEFT]:
        myObject.grow(10, 10)
    if current_keys[pygame.K_RIGHT]:
        myObject.grow(-10, -10)
#def

def draw_rect():
    myObject.draw()
    myObject1.draw()
    myObject2.draw()
    myObject3.draw()
    myObject4.draw()

def main():
    global current_keys
    current_keys = pygame.key.get_pressed()

    running = True
    Buttons.render()

    wheelCal_label = Label((myObject.x, myObject.y), 'Wheel Calibration', 50, (255, 255, 255))
    pidCal_label = Label((myObject1.x, myObject1.y), 'PID Calibration', 50, (255, 255, 255))
    speedCal_label = Label((myObject2.x, myObject2.y), 'Speed Calibration', 50, (255, 255, 255))
    monitor_label = Label((myObject3.x, myObject3.y), 'Shutdown Monitor', 50, (255, 0, 0))

    if running == True:
        expand_click()
        draw_rect()

if __name__ == "__main__":

    pygame.display.set_caption("Pi Wars")
    pygame.font.init()
    clock = pygame.time.Clock()
    while True:
        main()

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)




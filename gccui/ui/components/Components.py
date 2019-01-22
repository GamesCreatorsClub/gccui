import pygame, time, sys

BLACK = [0, 0, 0]
DARK_GRAY = [64, 64, 64]
GRAY = [128, 128, 128]

font = None


class Component:
    def __init__(self, rect):
        self.rect = rect
        self.mouse_is_over = False

    def draw(self, surface):
        pass

    def redefineRect(self, rect):
        self.rect = rect

    def mouseOver(self, mousePos):
        self.mouse_is_over = True

    def mouseLeft(self, mousePos):
        self.mouse_is_over = False

    def mouseDown(self, mousePos):
        pass

    def mouseUp(self, mousePos):
        pass


class RectangleDecoration(Component):
    def __init__(self, rect, colour):
        super(Button, self).__init__(rect)  # Call super constructor to store rectable
        self.colour = colour

    def draw(self, surface):
        pygame.draw.rect(surface, colour, self.rect)


class Button(Component):
    def __init__(self, rect, onClick=None, onHover=None, label=None):
        super(Button, self).__init__(rect)  # Call super constructor to store rectable
        self.onClick = onClick
        self.label = label
        if self.label is not None:
            self.label.rect = self.rect  # set label's position to buttons

    def redefineRect(self, rect):
        super(Button, self).redefineRect(rect)
        if self.label is not None:
            self.label.rect = self.rect  # set label's position to buttons

    def draw(self, surface):
        if self.mouse_is_over:
            pygame.draw.rect(surface, DARK_GRAY, self.rect)
        else:
            pygame.draw.rect(surface, GRAY, self.rect)

        if self.label is not None:  # this way 'label' can be anything - text, image or something custom drawn
            self.draw(surface)

    def grow(self, change_w, change_h):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width + change_w, self.rect.height + change_h)
        self.change_w = change_w
        self.change_h = change_h

    def mouseUp(self, mousePos):
        if self.rect.collidepoint(mousePos) and self.onClick is not None:
            self.onClick(self, mousePos)


class Label(Component):
    def __init__(self, rect, text, font_size, colour):
        super(Label, self).__init__(rect)  # Call super constructor to store rectable
        self.text = text
        self.font_size = font_size
        self.colour = colour

    def draw(self, surface):
        text_surface = font.render(self.text, 0, self.colour)
        surface.blit(text_surface, self.rect)


if __name__ == "__main__":

    # All methods defined here are only for 'testing' and won't be seen if this file is imported as 'library'
    selected_component = None
    known_components = []
    mousePos = (0, 0)
    mouseDown = False

    def main(known_components):
        global current_keys, running, mouseDown, mousePos, selected_component

        def find_component(components, mousePos):
            for component in components:
                if component.rect.collidepoint(mousePos):
                    return component
            return None

        current_keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
                if mouseDown and selected_component is not None:
                    # if we have pressed button over existing component we might want to give mouse movements back
                    selected_component.mouseOver(mousePos)
                else:
                    # if we just moved mouse and it happens to be over existing component it might want to know that
                    if selected_component is not None:
                        selected_component.mouseLeft(mousePos)
                    selected_component = find_component(known_components, mousePos)
                    if selected_component is not None:
                        selected_component.mouseOver(mousePos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseDown = True
                # mouse is pressed let's find if it was over existing component
                if selected_component is not None:
                    # component might want to know that we just started a click, drag, press or something...
                    selected_component.mouseDown(mousePos)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouseDown = False
                # mouse is released - if it was originally pressed over a component it might want to know that so it can trigger 'onClick' callback
                if selected_component is not None:
                    selected_component.mouseUp(mousePos)
                    if not selected_component.rect.collidepoint(mousePos):
                        # we released button outside of component - it would be nice to let it know mouse is not inside of it any more
                        selected_component.mouseLeft(mousePos)
                selected_component = find_component(known_components, mousePos)
                if selected_component is not None:
                    # we released mouse over some other component - now it is turn for it to receive mouse down
                    selected_component.mouseDown(mousePos)

        running = True

        for component in known_components:
            component.draw(screen)

        if running:  # if variable is boolean then v == True is same as v
            expand_click()


    def expand_click():
        # this is for the onClick() response
        if current_keys[pygame.K_LEFT]:
            myObject.grow(10, 10)
        if current_keys[pygame.K_RIGHT]:
            myObject.grow(-10, -10)


    def button1Pressed(button, pos):
        print("Button1 pressed")

    def button2Pressed(button, pos):
        print("Button2 pressed")

    def someButtonPressed(button, pos):
        print("Button3 or button 4 is pressed")

    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pi Wars")

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    running = True

    myObject = Button(pygame.Rect(320, 280, 80, 150))
    myObject1 = Button(pygame.Rect(myObject.rect.x + 300, myObject.rect.y, 80, 150), button1Pressed)  # making each button relative to the middle one.
    myObject2 = Button(pygame.Rect(myObject.rect.x, myObject.rect.y + 200, 80, 150), button2Pressed)  # This doesnt really work, Ill remove it later
    myObject3 = Button(pygame.Rect(myObject.rect.x, myObject.rect.y - 200, 80, 150), someButtonPressed)
    myObject4 = Button(pygame.Rect(myObject.rect.x - 300, myObject.rect.y, 80, 150), someButtonPressed)

    wheelCal_label = Label(pygame.Rect(myObject.rect.x, myObject.rect.y, 0, 0), 'Wheel Calibration', 50, (255, 255, 255))
    pidCal_label = Label(pygame.Rect(myObject1.rect.x, myObject1.rect.y, 0, 0), 'PID Calibration', 50, (255, 255, 255))
    speedCal_label = Label(pygame.Rect(myObject2.rect.x, myObject2.rect.y, 0, 0), 'Speed Calibration', 50, (255, 255, 255))
    monitor_label = Label(pygame.Rect(myObject3.rect.x, myObject3.rect.y, 0, 0), 'Shutdown Monitor', 50, (255, 0, 0))

    known_components.append(myObject)
    known_components.append(myObject1)
    known_components.append(myObject2)
    known_components.append(myObject3)
    known_components.append(myObject4)
    known_components.append(wheelCal_label)
    known_components.append(pidCal_label)
    known_components.append(speedCal_label)
    known_components.append(monitor_label)

    clock = pygame.time.Clock()
    while True:
        main(known_components)

        pygame.display.flip()
        clock.tick(60)




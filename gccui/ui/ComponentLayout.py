
class ComponentLayout(list):
    def __init__(self, surface, squares_across):
        self.grid_size = surface.get_width() / squares_across
        self.surface =  surface

    def append(self, *args, **kwargs):
        list.append(args, kwargs)
        for arg in args:
            arg.setLayoutManager(self)

    def draw(self):
        for

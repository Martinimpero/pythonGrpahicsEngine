from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self,obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        n, s = 80, 2
        for x in range(-n,n,s):
            for z in range(-n,n,s):
                add(Cube(app, pos=(x, -s, z)))

        add(Custom(app, 'cat', 'cat', pos=(0,-2,-10), rot=(-90,0,0)))

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()
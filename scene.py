import scenes.basic_tent_forest
from model import *
from scenes import *
import pygame as pg
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
        scenes.basic_tent_forest.load_scene(self, app)

    def initialize_scene(self):
        self.objects.clear()
        self.load()
        self.app.time = 0.0

    def toggle_debug(self):
        pass

    def update(self):

        scenes.basic_tent_forest.scene_update(self)
        # key events
        keys = pg.key.get_pressed()
        if keys[pg.K_F5]: self.initialize_scene()
        if keys[pg.K_F6]: self.toggle_debug()
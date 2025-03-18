from model import *
import numpy as np
def load_scene(scene, app):

    add = scene.add_object

    n, s = 20, 2
    for x in range(-n, n, s):
        for z in range(-n, n, s):
            add(Custom(app, vao_name='cushiony_thingy', tex_id=1, pos=(x, -s, z), rot=(0,0,0), scale=(0.20, 0.20, 0.20)))


    n, s = 20, 2
    for x in range(-n, n, s):
        for z in range(-n, n, s):
            if np.random.rand() > 0.5 and x != 0 and z != 0:
                add(Custom(app, vao_name='tree', tex_id='tree', pos=(x, -s + 1, z), rot=(0,0,0)))
def scene_update(self):
    pass
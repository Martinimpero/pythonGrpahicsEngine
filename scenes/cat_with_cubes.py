from model import *

def load_scene(scene, app):

    add = scene.add_object

    n, s = 20, 2
    for x in range(-n, n, s):
        for z in range(-n, n, s):
            add(Custom(app, vao_name='cushiony_thingy', tex_id=1, pos=(x, -s, z), rot=(0,0,0), scale=(0.20, 0.20, 0.20)))

    for i in range(9):
        add(Cube(app, pos=(15, i * s, -9 + i)))
        add(Cube(app, pos=(15, i * s, 5 - i)))

    add(Custom(app, 'cat', 'cat', pos=(0, -1, -10), rot=(-90, 0, 0), scale=(0.5,0.5,0.5)))

    scene.moving_cube = MovingCube(app, pos=(0,6,8), scale=(3,3,3), tex_id=0)
    add(scene.moving_cube)

def scene_update(self):
    self.moving_cube.rot.xyz = self.app.time
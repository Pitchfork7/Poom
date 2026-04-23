from ursina import *
import math

app = Ursina()

window.title = 'Poom'
window.exit_button.visible = False
window.fps_counter.enabled = True
window.color = color.black

speed = 1
platar = 1

ec = EditorCamera()

class planet:
    def __init__(self, name, age, texture, scale, pos, rad, orbtarget):
        self.name = name
        self.age = age
        self.texture = texture
        self.scale = scale
        self.pos = pos
        
        self.ob = Entity(model='cube', texture= self.texture, scale= self.scale, collider='box', position = self.pos)

        self.planetradius = rad
        self.planetangle = 0
        self.orbtarget = orbtarget
    def planorbit():
        self.planetangle += speed * time.dt
        self.ob.rotation_y += time.dt * 15
        self.ob.position = orbit(self.planetangle, self.planetradius, self.orbtarget)


# planets
earth = planet("Earth", 4.54, "textures/earth.png", 2, (0,0,0), 300, sun.ob)
moon = planet("Moon", 4.54, "textures/moon .png", 0.54, (0,0,0), 5, earth.ob)
sun = Entity(model='cube', texture='textures/sun.png', scale=109, collider='box', position=(0,0,0))
mars = planet("Mars", 4.54, "textures/mars.png", 1, (0,0,0), 500, sun.ob)

earthangle = 0
moonangle = 0
marsangle = 0

def update():
    global speed, earthangle, moonangle, marsangle, platar

    # cam pos
    if platar == 1:
        ec.position = earth.ob.position + Vec3(0, 10, -20)
    elif platar == 2:
        ec.position = mars.ob.position + Vec3(0, 10, -20)
    elif platar == 0:
        ec.position = sun.position

    sun.rotation_y += time.dt * 3

    # earth
    earthangle += speed * time.dt
    earthradius = 300
    earth.ob.rotation_y += time.dt * 15
    earth.ob.position = orbit(earthangle, earthradius, sun)

    moonangle += speed * time.dt
    moonradius = 5
    moon.ob.rotation_y += time.dt * 7
    moon.ob.position = orbit(moonangle, moonradius, earth.ob)

    marsangle += speed * 0.9 * time.dt
    marsradius = 500
    mars.ob.rotation_y += time.dt * 14
    mars.ob.position  = orbit(marsangle, marsradius, sun)

def input(key):
    global platar
    if key == '1':
        platar = 1
    elif key == "2":
        platar = 2
    elif key == "0":
        platar = 0

def orbit(angle, radius, target):
    return target.position + Vec3(math.cos(angle) * radius, 0, math.sin(angle) * radius)

app.run()

from ursina import *
import math
#app seetings
app = Ursina()

window.title = 'Poom'
window.exit_button.visible = False
window.fps_counter.enabled = True
window.color = color.black

#vars

speed = 1
platar = 1

ec = EditorCamera()

class planet:
    def __init__(self, name, age, texture, scale, pos, rad, orbtarget, rospeed, orbspeed):
        self.name = name
        self.age = age
        self.texture = texture
        self.scale = scale
        self.pos = pos
        
        self.ob = Entity(model='cube', texture= self.texture, scale= self.scale, collider='box', position = self.pos)

        self.rospeed = rospeed
        self.planetradius = rad
        self.planetangle = 0
        self.orbtarget = orbtarget
        self.orbspeed = orbspeed
    def planorbit():
        self.planetangle += self.orbspeed * time.dt
        self.ob.rotation_y += time.dt * self.rospeed
        self.ob.position = orbit(self.planetangle, self.planetradius, self.orbtarget)


# define planets
earth = planet("Earth", 4.54, "textures/earth.png", 2, (0,0,0), 300, sun, 15, 1)
moon = planet("Moon", 4.54, "textures/moon .png", 0.54, (0,0,0), 5, earth.ob, 5, 2)
sun = Entity(model='cube', texture='textures/sun.png', scale=109, collider='box', position=(0,0,0))
mars = planet("Mars", 4.54, "textures/mars.png", 1, (0,0,0), 500, sun, 14, 0.9)
venus = planet("venus",4.54, "textures/venus.png", 2, (0,0,0), 200, sun, 20, 1.5)


def update():
    global speed, platar

    # cam pos
    if platar == 1:
        ec.position = earth.ob.position + Vec3(0, 10, -20)
    elif platar == 2:
        ec.position = mars.ob.position + Vec3(0, 10, -20)
    elif platar == 0:
        ec.position = sun.position

    sun.rotation_y += time.dt * 3

    # orbits
    earth.planorbit()
    moon.planorbit()
    mars.planorbit()
    venus.planorbit()

    #inputs
def input(key):
    global platar
    #set plantar to correct number for cam pos
    if key == '1':
        platar = 1
    elif key == "2":
        platar = 2
    elif key == "0":
        platar = 0
#orbit func
def orbit(angle, radius, target):
    return target.position + Vec3(math.cos(angle) * radius, 0, math.sin(angle) * radius)

app.run()

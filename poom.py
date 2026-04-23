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

#planet class
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
    def planorbit(self):
        self.planetangle += self.orbspeed * time.dt
        self.ob.rotation_y += time.dt * self.rospeed
        self.ob.position = orbit(self.planetangle, self.planetradius, self.orbtarget)


# define planets
sun = Entity(model='cube', texture='textures/sun.png', scale=109, collider='box', position=(0,0,0))
earth = planet("Earth", 4.54, "textures/earth.png", 2, (0,0,0), 500, sun, 15, 1)
moon = planet("Moon", 4.54, "textures/moon.png", 0.54, (0,0,0), 5, earth.ob, 5, 2)
mars = planet("Mars", 4.54, "textures/mars.png", 1, (0,0,0), 700, sun, 14, 0.9)
venus = planet("venus",4.54, "textures/venus.png", 2, (0,0,0), 300, sun, 20, 1.5)


def update():
    global speed, platar

    # cam pos
    if platar == 1:
        target_pos = earth.ob.position
    elif platar == 2:
        target_pos = mars.ob.position
    elif platar == 0:
        target_pos = sun.position

    ec.position = lerp(ec.position, target_pos, 0.3)

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

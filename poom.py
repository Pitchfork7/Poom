from ursina import *

app = Ursina()

window.title = 'My Game'
window.exit_button.visible = False
window.fps_counter.enabled = True
window.color = color.black

speed = 1

ec = EditorCamera()

#planets
earth = Entity(model='cube', texture='textures/earth.png', scale=1, collider='box')
moon = Entity(model='cube', texture='textures/mars.png', scale=0.27, collider='box')
sun = Entity(model='cube', texture='textures/sun.png', scale=109, collider='box', position=(0,0,0))
mars = Entity(model='cube', texture='textures/mars.png', scale=0.5, collider='box')


def update():
    global speed
    #earth
    earthangle = speed * time.dt
    earthradius = 15
    earth.rotation_y += time.dt * 15
    earth.x = math.cos(earthangle) * earthradius
    earth.z = math.sin(earthangle) * earthradius

    moonangle = speed * time.dt
    moonradius = 15
    moon.rotation_y += time.dt * 15
    moon.x = math.cos(moonangle) * moonradius
    moon.z = math.sin(moonangle) * moonradius

    
    marsangle = speed * 0.9 * time.dt
    marsradius = 25
    mars.rotation_y += time.dt * 14
    mars.x = math.cos(marsangle) * marsradius
    mars.z = math.sin(marsangle) * marsradius



def input(key):
    if key == '1':
        ec.position = earth.position
    elif key == "2":
        #ec.position = mars.position
        pass
        
        
ec.position = earth.position
app.run()


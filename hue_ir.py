from time import sleep
import time
import random
from phue import Bridge
import lirc

bridgeIP = '192.168.88.250'


#use the IP of your bridge
b = Bridge(bridgeIP)
lights = b.get_light_objects()

def bluelights():
    color1 = 0.130
    color2 = 0.081
    for light in lights:
        light.xy = [color1, color2]

def redlights():
    color1 = 0.7
    color2 = 0.2986
    for light in lights:
        light.xy = [color1, color2]

def greenlights():
    color1 = 0.214
    color2 = 0.709
    for light in lights:
        light.xy = [color1, color2]

def yellowlights():
    color1 = 0.3227
    color2 = 0.329
    light_temp = 2874
    for light in lights:
        light.xy = [color1, color2]
        light.colortemp_k = light_temp

def toggle_lights():
    on = False
    for light in lights:
        if light.on:
            on = True
    if on:
        b.set_group(0,'on',False)
    else:
        b.set_group(0,'on',True)

def bright_up():
    for light in lights:
        if light.on and light.brightness<254:
            light.brightness+=40

def max_bright():
    for light in lights:
        light.brightness = 254

def dim_down():
    for light in lights:
        if light.on and light.brightness>0:
            light.brightness-=40

def max_dim():
    for light in lights:
        light.brightness = 0

def each_random():
    for light in lights:
        light.xy = [random.random(), random.random()]

def same_random():
    color1 = random.random()
    color2 = random.random()
    for light in lights:
        light.xy = [color1, color2]


def prog_1():
    alt = True
    color1 = [0.1859, 0.0771]
    color2 = [0.6367, 0.3349]
    for x in range(0, len(lights)):
        if alt:
            lights[x].xy = color1
            alt = False
        else:
            lights[x].xy = color2
            alt = True

def prog_2():
    alt = True
    color1 = [0.5136, 0.4444]
    color2 = [0.6349, 0.3413]
    for x in range(0, len(lights)):
        if alt:
            lights[x].xy = color1
            alt = False
        else:
            lights[x].xy = color2
            alt = True

buttons = {
  "blue": bluelights,
  "red": redlights,
  "green": greenlights,
  "yellow": yellowlights,
  "power": toggle_lights,
  "brighter": bright_up,
  "dimmer": dim_down,
  "maxbright": max_bright,
  "maxdim": max_dim,
  "1": prog_1,
  "2": prog_2,
  "0": each_random,
  "9": same_random,
}

while True:
    sockid = lirc.init('myprogram')
    button = lirc.nextcode()
    print button
    lirc.deinit()
    try:
        button = button[0]
        buttons[button]()
    except IndexError:
        print('index out of range, are you holding button?')



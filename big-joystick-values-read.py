import pygame

import time
from pygame import joystick

joystick.init()
pygame.display.init()
l=joystick.Joystick(0)
l.init()
while(1):
    pygame.event.pump()
    x=l.get_axis(0)
    y=l.get_axis(1)
    print(x,y)

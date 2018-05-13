import math as m
from pygame import joystick
import pygame
#import RPi.GPIO as GPIO

joystick.init()
pygame.display.init()
j=joystick.Joystick(0)
j.init()


while(1):
    pygame.event.pump()
    x=j.get_axis(0)
    y=j.get_axis(1)    
    x=x*255
    y=y*255
    print(x,y)
    

import math as m
from pygame import joystick
import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
#GPIO.setup(18,GPIO.OUT)
#GPIO.setup(19,GPIO.OUT)
p=GPIO.PWM(12,300)
q=GPIO.PWM(13,300)
#r=GPIO.PWM(18,300)
#s=GPIO.PWM(19,300)
x1=X=Y=xc=yc=0
def gpio(r,t,x,y):
    if r>1:
        r=1
    if x>=0 and y>=0:
        X=r*255
        xc=(X/255)*100
        if t<=45:
            Y=(r-(t/45)*r)*255
            yc=(Y/255)*100
            print("Forward Backward")
            p.ChangeDutyCycle(xc)
            q.ChangeDutyCycle(yc)
            #r.ChangeDutyCycle(0)
            #s.ChangeDutyCycle(yc)
        else:
            Y=(((t-45)/45)*r)*255
            yc=(Y/255)*100
            print("Forward Forward")
            p.ChangeDutyCycle(xc)
            q.ChangeDutyCycle(yc)
            #r.ChangeDutyCycle(0)
            #s.ChangeDutyCycle(0)
    elif x<=0 and y>=0:
        Y=r*255
        yc=(Y/255)*100
        if t<=45:
            X=(r-(t/45)*r)*255
            xc=(X/255)*100
            print("Backward Forward")
            p.ChangeDutyCycle(xc)
            q.ChangeDutyCycle(yc)
            #r.ChangeDutyCycle(xc)
            #s.ChangeDutyCycle(0)
        else:
            X=(((t-45)/45)*r)*255
            xc=(X/255)*100
            print("Forward Forward")
            p.ChangeDutyCycle(xc)
            q.ChangeDutyCycle(yc)
            #r.ChangeDutyCycle(0)
            #s.ChangeDutyCycle(0)
            
    elif x<=0 and y<=0:
        X=r*255
        xc=(X/255)*100
        if t<=45:
            Y=(r-(t/45)*r)*255
            yc=(Y/255)*100
            print("Backward Forward")
            p.ChangeDutyCycle(xc)
            q.ChangeDutyCycle(yc)
            #r.ChangeDutyCycle(xc)
            #s.ChangeDutyCycle(0)
        else:
            Y=(((t-45)/45)*r)*255
            yc=(Y/255)*100
            print("Backward Backward")
            p.ChangeDutyCycle(xc)
            q.ChangeDutyCycle(yc)
            #r.ChangeDutyCycle(xc)
            #s.ChangeDutyCycle(yc)        
    elif x>=0 and y<=0:
        Y=r*255
        yc=(Y/255)*100
        if t<=45:
            X=(r-(t/45)*r)*255
            xc=(X/255)*100
            print("Forward Backward")
            p.ChangeDutyCycle(xc)
            q.ChangeDutyCycle(yc)
            #r.ChangeDutyCycle(0)
            #s.ChangeDutyCycle(yc)
        else:
            X=(((t-45)/45)*r)*255
            xc=(X/255)*100
            print("Backward Backward")
            p.ChangeDutyCycle(xc)
            q.ChangeDutyCycle(yc)
            #r.ChangeDutyCycle(xc)
            #s.ChangeDutyCycle(yc)
    p.start(0)
    q.start(0)
    #r.start(0)
    #s.start(0)

def func(x,y):
    X = x*255
    Y = y*255
    return X,Y

joystick.init()
pygame.display.init()
j=joystick.Joystick(0)
j.init()
#print(j.get_name())
#print(j.get_init())
#c=j.get_numaxes()
#print(int(c))
#print(j.get_axis(0))
while(1):
    pygame.event.pump()
    x=j.get_axis(0)
    y=j.get_axis(1)     
    #print(j.get_axis(0),j.get_axis(1))
    #X,Y=func(x,y)
    #print(x,y)
    r = (x**2+y**2)**0.5
    if x==0:
        x1=0.0000000000000001
    else:
        x1=x
    t = m.degrees(m.atan(y/x1))
    gpio(r,m.fabs(t),x,-y)
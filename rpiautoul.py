#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER1 = 23
GPIO_ECHO1 = 24

GPIO_TRIGGER2 = 22
GPIO_ECHO2 = 27

md1g=19
md2g=26
md3g=16
md4g=20
md1p=19
md2p=26
md3p=16
md4p=20
#md1p=12
#md2p=13
#md3p=18
#md4p=19

#motor driver pins
GPIO.setup(md1g,GPIO.OUT)
GPIO.setup(md2g,GPIO.OUT)
GPIO.setup(md3g,GPIO.OUT)
GPIO.setup(md4g,GPIO.OUT)
GPIO.setup(md1p,GPIO.OUT)
GPIO.setup(md2p,GPIO.OUT)
GPIO.setup(md3p,GPIO.OUT)
GPIO.setup(md4p,GPIO.OUT)

p1=GPIO.PWM(md1p,300)
p2=GPIO.PWM(md2p,300)
p3=GPIO.PWM(md3p,300)
p4=GPIO.PWM(md4p,300)


 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def dis():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER2, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            leftd = distance()
            rightd = dis()
            print ("left Distance = %.1f cm" % leftd)
            print ("right Distance = %.1f cm" % rightd)
            if leftd < 10 and rightd < 10:
                GPIO.output(md1g,GPIO.LOW)
                GPIO.output(md2g,GPIO.HIGH)
                GPIO.output(md3g,GPIO.LOW)
                GPIO.output(md4g,GPIO.HIGH)
                p1.ChangeDutyCycle(100)
                p2.ChangeDutyCycle(100)
                p3.ChangeDutyCycle(100)
                p4.ChangeDutyCycle(100)
                print("move back")
                time.sleep(1)



            elif leftd < 10:
                GPIO.output(md1g,GPIO.LOW)
                GPIO.output(md2g,GPIO.HIGH)
                GPIO.output(md3g,GPIO.LOW)
                GPIO.output(md4g,GPIO.HIGH)
                p1.ChangeDutyCycle(100)
                p2.ChangeDutyCycle(100)
                p3.ChangeDutyCycle(100)
                p4.ChangeDutyCycle(100)
                print("move right")
                time.sleep(1)
                
            elif rightd < 10:
                GPIO.output(md1g,GPIO.HIGH)
                GPIO.output(md2g,GPIO.LOW)
                GPIO.output(md3g,GPIO.HIGH)
                GPIO.output(md4g,GPIO.LOW)
                p1.ChangeDutyCycle(100)
                p2.ChangeDutyCycle(100)
                p3.ChangeDutyCycle(100)
                p4.ChangeDutyCycle(100)
                print("move left")
                time.sleep(1)

            else:
                GPIO.output(md1g,GPIO.HIGH)
                GPIO.output(md2g,GPIO.HIGH)
                GPIO.output(md3g,GPIO.HIGH)
                GPIO.output(md4g,GPIO.HIGH)
                p1.ChangeDutyCycle(100)
                p2.ChangeDutyCycle(100)
                p3.ChangeDutyCycle(100)
                p4.ChangeDutyCycle(100)
                print("move forward")
                time.sleep(1)


            
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
import RPi.GPIO as GPIO
from gpiozero import Buzzer #This is for the buzzer I metntioned in the read me. If you
# dont want to add the buzzer ignore this and everything else that mentions buzzer.
GPIO.setmode(GPIO.BMC)
buzzer = Buzzer(18) #18 is the gpio pin that I use for the buzzer
GPIO.setup(24, GPIO.IN) #sets up the gpio pins the sensors will use. (pin 24)
xs = True
while xs:
  if(GPIO.input(24)):# This says if there isn't any input from the sensor then print off and
    #turn the buzzer off
    buzzer.off()
    print('off')
  else:
    buzzer.on()# This says if there is input turn the buzzer on and print on.
    print('on')

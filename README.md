# CollisionSensorsRaspBerryPi
Infrared collision sensor and collision sensor raspberry pi

The two key studio sensors this repository is about are the infrared collision sensor and the collision sensor.

![image](https://github.com/TylerDStanford/CollisionSensorsRaspBerryPi/assets/141964312/745b7d0d-9fb0-4b09-9f54-cfd6afecaa21)
- This is the regular collision sensor

![image](https://github.com/TylerDStanford/CollisionSensorsRaspBerryPi/assets/141964312/972dc13e-c0f1-4fbf-8c3f-bdf7f2ea41b9)
- This is the infrared collision sensor

The regular collision sensor is more analog in the sense that it detects collision (or input) from the metal prong protruding from the sensor. It detects the input by pushing the metal prong so that it clicks a button and lights up the LED on the sensor. This is useful for detecting crashes on RC cars or robots that move. It can be used to detect when a crash happened or be used to execute code when a crash does happen. It's important to note that this is a crash detector, not a crash predictor. You will only get input when the crash happens instead of when a crash might happen. So if you want to minimize damage on an RC car it might be helpful to use some other obstacle detector like the Infrared collision sensor.

The infrared collision sensor is a sensor that uses Infrared light rays to detect if obstacles are in close proximity to the sensor. The range of the sensor is 2-40 cm and can be changed by turning the blue/white mechanism counterclockwise or clockwise on the sensor. This can be helpful when it comes to moving robots as it can be used to anticipate a collision and be used to decelerate before the crash happens. You could also use this as some sort of motion detector although it might be less efficient compared to other motion detector sensors.

The two sensors have the same output (on or off) which makes it easy to take and use the input in programs. One example is to see whether the sensor is off or on and if it's on apply a beeping sound via a buzzer. Since they have the same output they can both be used by the code in the python file above.

Circuits:
  

![IMG_3112](https://github.com/TylerDStanford/CollisionSensorsRaspBerryPi/assets/141964312/4f7a6219-f056-4c32-ad78-17b6a6e4dd55)
![IMG_3113](https://github.com/TylerDStanford/CollisionSensorsRaspBerryPi/assets/141964312/8d90932b-9a53-4111-a68b-3796e455578c)

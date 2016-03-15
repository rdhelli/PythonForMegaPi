# Python For MegaPi
## How To Use
 * Compile and upload the Firmware to MegaPi ( https://github.com/Makeblock-Official/FirmwareForMegaPi )
 * On your Raspberry Pi, 
 ```
 git clone https://github.com/Makeblock-Official/PythonForMegaPi
 ```
 * Insert the initial code for starting MegaPi first.
```
 from lib.megapi import *
 bot = MegaPi()
 bot.start()
 ```
 * python your code

## Python API
 * Start
 	* MegaPi()
 	* start()
 * GPIO
 	* digitalWrite( pin, level )
 	* pwmWrite( pin, pwm )
 	* digitalRead( pin, **def** onResult )
 	* analogRead( pin, **def** onResult )
 * Motion
	* DC Motor
	  * **dcMotorRun**( port, speed )
	* Servo Motor
	  * **servoRun**( port, angle )
	* Encoder Motor
	  * **encoderMotorRun**( port, speed )
	  * **encoderMotorMove**( port, speed, display, **def** onFinish )
	  * **encoderMotorMoveTo**( port, speed, position, **def** onFinish )
	* Stepper Motor
	  * **stepperMotorRun**( port, speed )
	  * **encoderMotorMove**( port, speed, display, **def** onFinish )
	  * **encoderMotorMoveTo**( port, speed, position, **def** onFinish )
	  
 * Sensors
 	* Ultrasonic Sensor
 	* LineFollow Sensor
 	* Light Sensor
 	* Sound Sensor
 	* Temperature Sensor
 	* PIR Motion Sensor
 	* Touch Sensor
 	* LimitSwitch
 	* Humiture Sensor
 	* Gas Sensor
 	* Flame Sensor
 	* Button
 	* Potentiometer
 	* Joystick
 	* 3-Axis Accelerometer and Gyro Sensor
 	* Compass
 	
 * Display
 	* RGB Led
 	* 7-segment Display
 	* Led Matrix Display
 	* Serial LCD Display
 * Others
 	* DSLR Shutter

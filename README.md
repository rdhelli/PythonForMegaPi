# Python For MegaPi
## How To Use
 * Compile and upload the Firmware to MegaPi ( https://github.com/Makeblock-Official/FirmwareForMegaPi )
 * On your Raspberry Pi, 
 ```
 git clone https://github.com/Makeblock-Official/PythonForMegaPi
 ```
 *  In your python code, insert the init code for start MegaPi first.
```
 import lib.megapi from *
 
 bot = MegaPi()
 
 bot.start()
 ```
 * python your code

## Python API
 * Start
 	* MegaPi()
 	* start()
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
 
 * Display

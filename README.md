# Python For MegaPi
## How To Use
### Prepare for Arduino
 * Download the Arduino library for Makeblock https://github.com/Makeblock-official/Makeblock-Libraries/archive/master.zip
 * Copy the makeblock folder to your arduino default library. Your Arduino library folder should now look like this 
   * (on Windows): ```[x:\Users\XXX\Documents]\Arduino\libraries\makeblock\src```
   * (on Mac OSX): ```[\Users\XXX\Documents]\Arduino\libraries\makeblock\src```
 * Open Arduino IDE, choose the firmware from <em>File&gt;Examples</em>.
 ![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/firmware.jpg)
 * Compile and upload firmware according to your board type.

### Prepare for Raspberry Pi
 * On your Raspberry Pi, disable the login prompt from Desktop->Menu->Preferences->Raspberry Pi Configuration.

![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/serial.jpg)
 * install python library for Makeblock
 ```
 sudo pip install megapi
 ```
 * the initial code for python.
```
 from megapi import *
 bot = MegaPi()
 bot.start() #if using usb cable, need to call bot.start('/dev/ttyACM0')
 ```
 * python your code

### Wiring
* Using MegaPi
 ![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/megapi.jpg)
* Using Me Shield for Raspberry Pi and RJ25 cable for Me Orion or Me Baseboard.
 ![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/baseboard-pi-shield.jpg)
* Using USB Cable for Me Orion or Me Baseboard
 ![image](https://raw.githubusercontent.com/Makeblock-official/PythonForMegaPi/master/images/baseboard-usb-cable.jpg)

## Python API
 * Start
 	* **MegaPi**()
 	* **start**()
 	
 * GPIO
 	* **digitalWrite**( pin, level )
 	* **pwmWrite**( pin, pwm )
 	* **digitalRead**( pin, **def** onResult )
 	* **analogRead**( pin, **def** onResult )
 	
 * Motion
	* DC Motor
	  * **motorRun**( port, speed )
	  * **motorMove**( leftspeed, rightspeed )
	* Servo Motor
	  * **servoRun**( port, slot, angle )
	* Encoder Motor
	  * **encoderMotorRun**( port, speed )
	  * **encoderMotorMove**( port, speed, distance, **def** onFinish )
	  * **encoderMotorMoveTo**( port, speed, position, **def** onFinish )
	* Stepper Motor
	  * **stepperMotorSetting**( port, microsteps, acceleration )
	  * **stepperMotorRun**( port, speed )
	  * **stepperMotorMove**( port, speed, distance, **def** onFinish )
	  * **stepperMotorMoveTo**( port, speed, position, **def** onFinish )
	  
 * Sensors
 	* Ultrasonic Sensor
 	  * **ultrasonicSensorRead** ( port, **def** onResult ) 
 	* LineFollow Sensor
 	  * **lineFollowerRead** ( port, **def** onResult ) 
 	* Light Sensor
 	  * **lightSensorRead** ( port, **def** onResult ) 
 	* Sound Sensor
 	  * **soundSensorRead** ( port, **def** onResult ) 
 	* Temperature Sensor
 	  * **temperatureRead** ( port, **def** onResult ) 
 	* PIR Motion Sensor
 	  * **pirMotionSensorRead** ( port, **def** onResult ) 
 	* Touch Sensor
 	  * **touchSensorRead** ( port, **def** onResult ) 
 	* LimitSwitch
 	  * **limitSwitchRead** ( port, slot, **def** onResult ) 
 	* Humiture Sensor
 	  * **humitureSensorRead** ( port, type, **def** onResult ) 
 	* Gas Sensor
 	  * **gasSensorRead** ( port, **def** onResult )
 	* Flame Sensor
 	  * **flameSensorRead** ( port, **def** onResult ) 
 	* Button
 	  * **buttonRead** ( port, **def** onResult ) 
 	* Potentiometer
 	  * **potentiometerRead** ( port, **def** onResult )
 	* Joystick
 	  * **joystickRead** ( port, axis, **def** onResult )
 	* 3-Axis Accelerometer and Gyro Sensor
 	  * **gyroRead** ( axis, **def** onResult )
 	* Compass
 	  * **compassRead** ( **def** onResult )
 	* Pressure Sensor for BMP085 and BMP180
 	  * **pressureSensorBegin** ( ) 
 	  * **pressureSensorRead** ( type, **def** onResult ) #1:Pressure #2:Temperature #3:Altitude #4:Real altitude #5:Sealevel Pressure
 	
 * Display
 	* RGB Led
 	  * **rgbLedSetColor** ( port, slot, index, r, g, b )
 	  * **rgbLedShow** ( port, slot )
 	  * **rgbLedDisplay** ( port, slot, index, r, g, b )
 	* 7-segment Display
 	  * **sevenSegmentDisplay** ( port, value )
 	* Led Matrix Display
 	  * **ledMatrixDisplayMessage** ( port, x, y, msg )
 	  * **ledMatrixDisplayRaw** ( port, buffer )
 	* Serial LCD Display
 	  * **lcdDisplay** ( string )
 	  
 * Others
 	* DSLR Shutter
	  * **shutterOn** ( port )
	  * **shutterOff** ( port )
	  * **focusOn** ( port )
	  * **focusOff** ( port )

###Learn more from Makeblock official website: www.makeblock.com

###恢复硬件串口的方法
1. 下载pi3-miniuart-bt-overlay
http://ukonline2000.com/?attachment_id=881

2.编辑/boot目录下的config.txt文件
sudo nano /boot/config.txt
添加下面两行:
dtoverlay=pi3-miniuart-bt-overlay
force_turbo=1

3.编辑/boot目录下的cmdline.txt文件
sudo nano /boot/cmdline.txt
参考下面内容修改:
dwc_otg.lpm_enable=0 console=serial1,115200  console=tty1 root=/dev/mmcblk0p2  kgdboc=serial1,115200 rootfstype=ext4 elevator=deadline fsck.repair=yes  rootwait

###关闭板载蓝牙的方法
1.SSH登录树莓派3后，输入下面命令关闭hciuart使用uart0.
sudo systemctl disable hciuart
2.编辑/lib/systemd/system/hciuart.service 将 “ttyAMA0”修改为“ttyS0”
sudo nano /lib/systemd/system/hciuart.service
将 “ttyAMA0”修改为“ttyS0”
3.重启
树莓派默认用户名和密码：
pi
raspberry

apt-get install python-pip
apt-get install pyserial

###安装串口调试工具
apt-get install minicom
连接串口
minicom -b 115200 -o -D /dev/ttyAMA0

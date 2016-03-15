from lib.megapi import *

if __name__ == '__main__':
	bot = MegaPi()
	bot.start()
	while True:
		sleep(1);
		bot.servoRun(0,40);
		sleep(1);
		bot.servoRun(0,120);
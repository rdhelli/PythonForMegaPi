from lib.megapi import *

def onForwardFinish():
	sleep(0.4);
	bot.stepperMoveTo(1,0,500,onBackwardFinish);

def onBackwardFinish():
	sleep(0.4);
	bot.stepperMoveTo(1,1000,500,onForwardFinish);

if __name__ == '__main__':
	bot = MegaPi()
	bot.start()
	bot.stepperStop(1);
	sleep(1);
	onForwardFinish();
	while 1:
		continue;
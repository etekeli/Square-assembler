from time import sleep

from ivy.ivy import IvyServer
from ivy.std_api import *
from ivy.ivy import *

IVYAPPNAME = ''


def lprint(fmt, *arg):
	print(IVYAPPNAME + ': ' + fmt % arg)


def onhello(agent, *larg):
	sreply = 'goodday %s from=%s ' % (larg[0], IVYAPPNAME)
	lprint('on hello , replying to %r: [%s]', agent, sreply)
	IvySendMsg(sreply)


def ontick():
	lprint('%s send a tick', IVYAPPNAME)
	IvySendMsg('%s_tick' % IVYAPPNAME)


def die(self):
	self.stop()


def on_connection_change(agent, event):
	if event == IvyApplicationDisconnected:
		info('Ivy application %r has conencted', agent)
	else:
		info('Ivy application %r has conencted', agent)
		info('List applications on bus : %s ', ','.join(IvyGetApplicationList()))


def main():
	IvyInit('agent', "Square server [Pret]", 0, on_connection_change, die)
	IvyStart("127.0.0.1:25565")
	IvyBindMsg(onhello, 'hello .*')

	timerid = IvyTimerRepeatAfter(0, 1000, ontick)  # handler to call
	IvyMainLoop()

import json
import uuid

from ivy.ivy import IvyProtocolError
from ivy.std_api import *

IVYAPPNAME = 'SquareAssembler'
sisreadymsg = '[%s is ready]' % IVYAPPNAME

CONNECTION_ATTEMPT = {'state': '_connection_attempt'}
CONNECTION_CANCELED = {'state': '_connection_canceled'}
CONNECTION_ACCEPTED = {'state': '_connection_accepted'}
INIT_GAME = '_init_game'
LOAD_GAME = '_load_game'
UPDATE_GAME = '_update_game'
MOVE_PLAYED = '_move_played'
SEND_MOVE = '_send_move'
HOST_MOVE = '_host_move'
REMOTE_MOVE = '_remote_move'
END_GAME = '_end_game'


def info(fmt, *arg):
	print(fmt % arg)


class Agent:
	def __init__(self, name, controller):
		"""
		Constructeur d'agent Ivy
		Params:
		name: Nom de notre agent
		controller: GameController
		"""
		self.enemy = None
		self.name = IVYAPPNAME + '_' + name
		self.adresse = ''
		self.controller = controller
		try:
			IvyInit(f'{self.name}{uuid.uuid4()}')
		except:
			pass
		IvyStart(self.adresse)
		self.controller.view.protocol('WM_DELETE_WINDOW', self.endExit)
		self.init()
		IvyBindDirectMsg(self.on_direct_msg)
		self.init_timer()

	def endExit(self):
		self.controller.supprimer()
		sys.exit()

	def __del__(self):
		print("stooop")
		self.controller.supprimer()

	def init(self):
		pass

	def on_direct_msg(self, agent, _id, msg):
		pass

	def on_connection_change(self, agent, event):
		if event == IvyApplicationDisconnected:
				info('%r disconnnected', agent)
				#IvyStop()
				self.controller.view.gameCanvas.showGameOver()
		else:
				info('%r connnected', agent)

	def on_die(self, agent, id):
		info("Received the order to die from %r with id = %d", agent, id)

	def stop_app(self):
		if self.enemy is not None:
			print("stooooop")
			IvyStop()
			self.enemy = None
			# self.controller.view.destroy()

	def send_msg(self, msg, agent=None):
		"""
		Envoi un message direct à l'agent, si agent None l'envoi à l'enemi
		params:
		`msg` : Tableau qui sera convertit en JSON
		`agent` : Agent Ivy à contacter
		"""
		msg_json = json.dumps(msg)
		IvySendDirectMsg((agent if agent is not None else self.enemy), 0, msg_json)

	def init_timer(self):
		self.timerid = IvyTimerRepeatAfter(0, 1000, self.on_tick)	# repeat, time ms, callback

	def on_tick(self):
		pass

	def on_msg(agent, *arg):
		info("Received from %r: %s", agent, arg and str(arg or '<no args>'))

	def msg_rcvd(agent, num_id, msg):
		print("received message")


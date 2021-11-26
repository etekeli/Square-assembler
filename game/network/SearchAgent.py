from game.network.Agent import *


class SearchAgent(Agent):
		"""
		Agent utilisé pour se connecter à une partie
		"""

		def __del__(self):
			super().__del__()

		def __init__(self, name, controller):
			super().__init__(name, controller)

		def init(self):
			IvyBindMsg(self.on_hosting_agent, '(_hosting)')

		def on_hosting_agent(self, agent, msg):
			if self.enemy is None:
				self.send_msg(CONNECTION_ATTEMPT, agent)

		def on_direct_msg(self, agent, _id, msg_json):
			msg = json.loads(msg_json)
			info('Direct message : %r', msg)
			# Notre serveur accepte la connexion
			if msg['state'] == CONNECTION_ACCEPTED['state']:
				# Si déjà un enemi -> On annule la connexion
				if self.enemy is not None:
						self.send_msg(CONNECTION_CANCELED, agent)
					# Sinon on accepte, on init la game, mais on renvoi pas de deny
				else:
					self.enemy = agent
					self.controller.notify(msg)
					info("Enemy connected, %r", agent)
			else:
				self.controller.notify(msg)

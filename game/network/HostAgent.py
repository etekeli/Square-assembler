from pprint import pprint
from game.network.Agent import *


class HostAgent(Agent):
    """
    Agent utilisé pour héberger la partie
    """

    def __init__(self, name, controller):
        super().__init__(name, controller)

    def on_direct_msg(self, agent, _id, msg_json):
        msg = json.loads(msg_json)
        info('Message reçu : %r', msg)

        if msg['state'] == CONNECTION_ATTEMPT['state']:
            if self.enemy is None:
                self.enemy = agent
                self.send_msg(CONNECTION_ACCEPTED)
                info("Un adversaire est connecté, agent : " + str(agent))

                pprint(msg)
                self.controller.notify({
                    'state': INIT_GAME,
                    'agent': agent,
                    'level': 10
                })
        elif msg['state'] == CONNECTION_CANCELED['state']:
            if self.enemy is agent and self.enemy is not None:
                self.enemy = None
        else:
            self.controller.notify(msg)

    def on_tick(self):
        if self.enemy is None:
            IvySendMsg("_hosting")

    def die(self):
        pass

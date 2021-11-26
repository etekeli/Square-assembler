from threading import Thread
from time import sleep
from ivy.ivy import *


sisreadymsg = '[Server ready]'


class GameServer(IvyServer, Thread):
    def __init__(self, agent_name, isServer, cont):
        IvyServer.__init__(self, agent_name + str(isServer), 'hello user', app_callback=on_connection_change, die_callback=on_die)  # , sisreadymsg, 0, on_connection_change, die
        self.controller = cont
        self.server_address = ('127.0.0.1', 25565)
        self.start()
        self.bind_msg(on_msg, "^game_game_ (.*)")
        print("Server : " + str(self.isAlive()) + " - " + self.agent_name + " - Port :" + str(self.port))


def on_msg(agent, *args, **kw):
    print('[Agent %s] GOT hello from r')
    #if agent.agent_name != 'TEST_APP' and agent.agent_name != self.agent_name:
    #print(f'Received from {agent}: ', arg and str(arg) or '<no args>')


def on_die(agent, *args, **kw):
    agent.stop()


def on_connection_change(agent, event):
    #if agent.agent_name != 'TEST_APP': #and agent.agent_name != self.agent_name:
    if event == IvyApplicationDisconnected:
        print(f'{agent.name} disconnected')
    else:
        print(f'{agent.name} connected')

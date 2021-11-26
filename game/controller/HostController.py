from game.controller.GameController import GameController
from game.model.models.HostModel import HostModel
from game.network.Agent import *
from game.network.HostAgent import HostAgent


class HostController(GameController):
    def __init__(self, view):
        super().__init__(view, HostModel(self))
        self.network = None

    def newGame(self, dialog, ip=None):
        self.waitingDialog = dialog
        self.network = HostAgent("Host", self)

    def stop(self):
        print("stop")
        if self.network is not None:
            self.network.stop_app()
            self.network = None

    def supprimer(self):
        print("Controller stop")
        if self.network is not None:
            self.network.send_msg({'state': END_GAME})
            self.stop()

    def notify(self, msg):
        """
        Notification au controller
        Params:
        msg['state'] : INIT_GAME
        """

        print(f'Notification HostController :  {msg}')
        if msg['state'] == INIT_GAME:
            self.waitingDialog.destroy()
            self.model.newGame(msg['level'], msg['agent'].agent_name)
            self.showAll()
            self.network.send_msg({'state': LOAD_GAME, 'game': self.model.toArray()})
        elif msg['state'] == UPDATE_GAME:
            self.model.player.turn = True
            self.waitingDialog.destroy()
            self.model.load(msg['game'])
            self.showAll()
        elif msg['state'] == HOST_MOVE:
            print("Host : Vous avez joué en " + str(msg['i'])+" ; " +str(msg['j']))
            self.play(msg['i'], msg['j'])
            self.network.send_msg(msg)
        elif msg['state'] == REMOTE_MOVE:
            print("Enemy Remote : A joué en " + str(msg['i'])+" ; " + str(msg['j']))
            self.model.enemyPlay(msg['i'], msg['j'])
            self.checkGameOver()
        elif msg['state'] == END_GAME:
            self.forceGameOver()
            self.stop()

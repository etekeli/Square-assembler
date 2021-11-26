from game.controller.GameController import GameController
from game.model.models.RemoteModel import RemoteModel
from game.network.Agent import *
from game.network.SearchAgent import SearchAgent


class RemoteController(GameController):
    def __init__(self, view):
        super().__init__(view, RemoteModel(self))
        self.network = None

    def newGame(self, dialog, ip=None):
        self.waitingDialog = dialog
        self.network = SearchAgent("Search", self)

    def stop(self):
        print("stop")
        if self.network is not None:
            self.network.stop_app()
            self.network = None

    def supprimer(self):
        if self.network is not None:
            self.network.send_msg({'state': END_GAME})
            self.stop()

    def notify(self, msg):
        """
        Notification au controller
        Params:
        msg['state'] : INIT_GAME
        """
        print(f'Notification RemoteController :  {msg}')
        if msg['state'] == LOAD_GAME:
            self.waitingDialog.destroy()
            self.model.load(msg['game'])
            self.showAll()
        elif msg['state'] == UPDATE_GAME:
            self.model.player.turn = True
            self.waitingDialog.destroy()
            self.model.load(msg['game'])
            self.showAll()
        elif msg['state'] == REMOTE_MOVE:
            print("Remote : Vous avez joué en "+ str(msg['i']) +" ; "+ str(msg['j']))
            self.play(msg['i'], msg['j'])
            self.network.send_msg(msg)
        elif msg['state'] == HOST_MOVE:
            print("Enemy Host : A joué en "+ str(msg['i']) +" ; "+ str(msg['j']))
            self.model.enemyPlay(msg['i'], msg['j'])
            self.checkGameOver()
        elif msg['state'] == END_GAME:
            self.forceGameOver()
            self.stop()

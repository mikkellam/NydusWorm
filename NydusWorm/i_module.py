from abc import ABC, abstractmethod


class IModule(ABC):
    @abstractmethod
    def initialise(self):
        """Callback method. Called when framework is launched"""
        print("implement initialise")

    @abstractmethod
    def game_start(self):
        """callback method. Called when the sc2 game is started"""
        print("implement game_start")

    @abstractmethod
    def game_step(self):
        """callback method. called every step in step mode or every frame in real-time"""
        print("implement game_step")

    @abstractmethod
    def game_ended(self):
        """callback method. called when the sc2 game ends"""
        print("implement game_ended")

    @abstractmethod
    def restart(self):
        """callback method. called when the game restarts"""
        print("implement restart")

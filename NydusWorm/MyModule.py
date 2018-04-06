from IAsyncModule import IAsyncModule


class MyModule(IAsyncModule):
    def __init__(self, proxy_man):
        IAsyncModule.__init__(self, proxy_man)

    def initialise(self):
        print("Do something before the game starts")

    def game_start(self):
        print("Do as the game starts")
        self.request_intel_update()  # request intel when you need it rather than getting it each step.

    def game_ended(self):
        print("When the game ends")

    def restart(self):
        print("Do somthing as the game restarted")

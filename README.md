This is the Python proxy for the Abathur Framework And allow for the creation of Starcraft 2 AI's. To get started with programming your AI in python follow these steps.

### 1

make sure you have the lastest vesion of starcraft II installed on your PC.

### 2 

Check that you have the dotnetcore sdk installed.

 ```
 dotnet --version
 ```
the proxy is tested on dotnet version 2.1.103

### 3

Ensure python is installed. 
```
 python --version
```
proxy has been written to 3.6.4


### 4

open a console and run the Launcher.dll 

```
dotnet Launcher.dll
```
running the launcher for the first time will generate the settingsfiles in \data from where you can maniuplate them to your liking. Enjoy our random demo playing against a very easy bot or shut down the program and continue to step 5.

### 5

If you do not have protobuf for python installed you will have to do so. For Windows users you can run "WinInstallProtobuf" from the commando promp and this will be done for you. However for linux and mac you will have to download or compile the [appropriate protoc binaries](https://github.com/google/protobuf/releases/tag/v3.5.1) and run the setup.py as:
```
python setup.py build
python setup.py test
python setup.py install
```
or see [googles own guide](https://github.com/google/protobuf/tree/master/python)

### 6

Now you will have to write your python module, but to check that everything is working first try running one of the dummy modules: Go to \data and open the setup.json file and remove the "EmptyModule","RandomDemo" and "AutoSupply" modules from the json and add the command to run the DummyLauncher.py file as a module instead. eg add "python "{path}\\DummyLauncher.py"". Furthermore if you want to make sure the dummymodule does somthing open gamesettings.json and change `"ParticipantRace":4,` to `"ParticipantRace":1,` indicating that the participant will be playing terran and not random. Now run the Launcher again like in step 4.

### 7

If everything has worked up till now you will now simply have create a class implementing from IModule or IAsyncModule. We reccomend implementing an IAsyncModule as the python proxy is much slower than the c# stepmodules. 
```
class MyModule(IAsyncModule):
    def __init__(self, proxy_man):
        IAsyncModule.__init__(self, proxy_man)
        
    def initialise(self):
        print("Do something before the game starts")

    def game_start(self):
        print("Do as the game starts")
        self.request_intel_update() # request intel when you need it rather than getting it each step.

    def game_ended(self):
        print("When the game ends")

    def restart(self):
        print("Do somthing as the game restarted")
```

### 8

once you have a class implementing from one of the IModules you need to add it to the gameloop. For this you need a class inheriting from Nydusworm and implementing the method add_modules(You can just use the DummyLauncher.py):

```
import sys
from NydusWorm import NydusWorm
from dummy_async_module import dummy_async_module
from dummy_module import DummyModule
from ProductionManager import ProductionManager
from CombatManager import CombatManager
from IntelManager import IntelManager


class DummyLauncher(NydusWorm):
    def add_modules(self, manager, services):
        prod_man = services.get(ProductionManager)
        combat_man = services.get(CombatManager)
        intel_man = services.get(IntelManager)
        #manager.add_module(DummyModule(prod_man, intel_man, combat_man))
        manager.add_module(dummy_async_module(manager, intel_man, combat_man, prod_man))


launcher = DummyLauncher()
launcher.launch_framework(sys.argv)
```

"manager" is the ProxyManager that is in charge of communication with the c# framework and gives access to rawRequests along with being used for most of the proxy's internal control. Every async module will need to take this in their __init__ method to be able to request intel.

"services" is a dictionary going from the type of a service to the only allowed instance of that type in the program. The services provides diffrent functionalities that will make the AI programming a lot easier than using rawRequests. The available services are:
ProductionManager
CombatManager
IntelManager
AbilityRepository
BuffRepository
UnitTypeRepository
UpgradeRepository
RequirementRepository

Their functionalities are simmilar to the one of their equivalents in the [c# framework](https://github.com/schmidtgit/AbathurBot/blob/master/AbathurBot/Modules/FullModule.cs). 


### 9

Make a cool AI. For more detailed information about the framework and it's functionality check out [AbathurBot](https://github.com/schmidtgit/AbathurBot), Abathurs homepage [https://adequatesource.com/](https://adequatesource.com/) or the full [c# framework](https://github.com/schmidtgit/Abathur)

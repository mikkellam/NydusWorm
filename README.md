This is the Python proxy for the Abathur Framework And allows for the creation of Starcraft 2 AI's. To get started with programming your AI in python follow these steps.

### Step 1

Make sure you have:

[Starcraft II](https://starcraft2.com/)

[The dotnetcore SDK(version 2.1.103)](https://www.microsoft.com/net/download/windows)

[Python(3.6.4)](https://www.python.org/downloads/)

[Protobuf for python](#get-protobuf)

Forked this repo

### Step 2 
Open a console in the repo and run the Launcher.dll 

```
dotnet Launcher.dll
```
Running the launcher for the first time will generate the settingsfiles in \data from where you can maniuplate them to your liking. Enjoy our async module playing against a very easy bot or shut down the program and continue to step 3.

### Step 3

If everything has worked up till now you will have to create a class implementing from IModule or IAsyncModule. We reccomend implementing an IAsyncModule as the python proxy is much slower than the c# stepmodules. For instance use MyModule.py as a starting point.

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

### Step 4

Once you have a class implementing from one of the IModules you need to add it to the gameloop. For this you need a class inheriting from Nydusworm and implementing the method add_modules(You can just use the DummyLauncher.py):

```
import sys
from NydusWorm import NydusWorm
from DummyAsyncModule import DummyAsyncModule
from DummyModule import DummyModule
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
[What is manager and services?](#what-are-the-parameters-to-add_module)

### Step 5
Once you have added the module in the launcher, if you used DummyLauncher.py you can simply run the program like in step 2. Otherwise you will have to go to \data, open the setup.json file and replace Dummylauncher.py with the name of your launcher in

"\\"python NydusWorm\\\\DummyLauncher.py\\"" 

[what is this string?](#what-is-the-module-string)

### Step 6
Improve your AI. 

## More information
For more detailed information about the framework and it's functionality check out [AbathurBot](https://github.com/schmidtgit/AbathurBot), Abathurs homepage [https://adequatesource.com/](https://adequatesource.com/) or the full [c# framework](https://github.com/schmidtgit/Abathur)

## Get Protobuf
If you do not have protobuf for python installed you will have to do so. For Windows users you can run "WinInstallProtobuf" from the commando promp and this will be done for you. However for linux and mac you will have to download or compile the [appropriate protoc binaries](https://github.com/google/protobuf/releases/tag/v3.5.1) and run the setup.py as:
```
python setup.py build
python setup.py test
python setup.py install
```
or see [googles own guide](https://github.com/google/protobuf/tree/master/python)

## What are the parameters to add_module
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

Their functionalities are simmilar to the ones of their equivalents in the [c# framework](https://github.com/schmidtgit/AbathurBot/blob/master/AbathurBot/Modules/FullModule.cs). 


## What is the module string
The string added when you add a module to the setupfile is the command to run the DummyLauncher.py file as a module instead of the class name of the module. eg add:

"python "{path}\\\\DummyLauncher.py""

runs dummy launcher with the framework. You cannot simply run this command from the command line as there will be a port added to the arguments from c# at runtime.

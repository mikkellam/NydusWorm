import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import threading
import abathur_pb2
import essence_pb2
import proxy_manager
import IAsyncModule
import IModule
from AbilityRepository import AbilityRepository
from BuffRepository import BuffRepository
from UnitTypeRepository import UnitTypeRepository
from UpgradeRepository import UpgradeRepository
from RequirementRepository import RequirementRepository
from CombatManager import CombatManager
from ProductionManager import ProductionManager
from IntelManager import IntelManager
from abc import ABC, abstractmethod
essence_path = ".\\data\\essence.data"


class NydusWorm(ABC):
    """Launcher class for the python proxy. extend this, implement "add_modules"
       and call "launch_framework" to connect to c#"""
    def __init__(self):
        self.man = None
        self.only_async = True

    def handle_notification(self, manag, m):
        """Calls appropriate modules callback depending on notification type

        :param manag:ProxyManager containing the active modules
        :param m:the notification being handled
        :return:
        """
        if m.notification.type == abathur_pb2.Initialize:
            for module in manag.modules:
                module.initialise()
            return False
        if m.notification.type == abathur_pb2.GameStart:
            for module in manag.modules:
                module.game_start()
            return True
        if m.notification.type == abathur_pb2.GameStep:
            for module in manag.modules:
                if not isinstance(module, IAsyncModule.IAsyncModule):
                    module.game_step()
            return True
        if m.notification.type == abathur_pb2.GameEnded:
            for module in manag.modules:
                module.game_ended()
            return True
        if m.notification.type == abathur_pb2.Restart:
            for module in manag.modules:
                module.restart()
            return True
        return True

    @abstractmethod
    def add_modules(self, manager, services):
        """Adds all modules that should be called during program execution

        :param manager: The ProxyManager giving access to rawcommands and managing the connection  to c#
        :param services: a dictionary holding {type : service} pairs.
        :return:
        """
        print("add all the modules you want to run in the framework")

    def load_essence_file(self, path):
        """load the essence file from disk and construct services with the data

        :param path: string representing the path to the essence.data file
        :return:
        """
        services = {}
        es = essence_pb2.Essence()
        f = open(path, "rb")
        es.ParseFromString(f.read())
        f.close()
        print("Essence data version: " + es.DataVersion + " with build: " + str(es.DataBuild))
        abi_repo = AbilityRepository(es.abilities)
        buff_repo = BuffRepository(es.buffs)
        unit_repo = UnitTypeRepository(es.unitTypes)
        upg_repo = UpgradeRepository(es.upgrades)
        req_repo = RequirementRepository(es.unitProducers,es.unitRequiredBuildings,
                                         es.researchProducer, es.researchRequiredBuildings,
                                         es.researchRequiredResearch)

        services.update({type(abi_repo): abi_repo})
        services.update({type(buff_repo): buff_repo})
        services.update({type(unit_repo): unit_repo})
        services.update({type(upg_repo): upg_repo})
        services.update({type(req_repo): req_repo})

        return services

    def launch_framework(self, args):
        """Connect to C#, setup services and mediate communication to c#

        :param args: string array of args containing the port to connect to
        :return:
        """
        if len(args) is not 2:
            print("incorrect arguments. proper usage: \npython <NydusWorm childs filename>.py <port>")
            return

        p = int(args[1])
        try:
            self.man = proxy_manager.ProxyManager(p)
            print("Python is Connected")
            services = self.load_essence_file(essence_path)
            services.update({CombatManager: CombatManager(self.man)})
            services.update({ProductionManager: ProductionManager(self.man)})

            intel_man = IntelManager()
            services.update({type(intel_man): intel_man})
            self.add_modules(self.man, services)
            for mod in self.man.modules:
                if isinstance(mod, IModule.IModule):
                    self.only_async = False

            t = threading.Thread(target=self.man.receive)
            t.start()

            while t.isAlive():
                while (not self.man.msg_queue.empty()) or (self.only_async and not self.man.answers.empty()):
                    if not self.man.msg_queue.empty():
                        m = self.man.msg_queue.get()
                        if m.HasField("intel"):
                            intel_man.update_intel(m.intel)
                            self.man.intel_received.set()
                        if m.HasField("rawResponse"):
                            print("Error. RawResponses should have been handled in receive")
                        if m.HasField("notification"):
                            if not self.handle_notification(self.man, m):
                                continue

                    for request in intel_man.squad_repository.requests:
                        self.man.answers.put(request)
                    for squad in intel_man.squad_repository.squads.values():
                        for request in squad.requests:
                            self.man.answers.put(request)
                        squad.requests.clear()
                    intel_man.squad_repository.requests.clear()

                    if not self.man.answers.empty():
                        ab_request = abathur_pb2.AbathurRequest()
                        while not self.man.answers.empty():
                            request = self.man.answers.get()
                            if isinstance(request, abathur_pb2.CombatRequest):
                                ab_request.combat.extend([request])
                            else:
                                if isinstance(request, abathur_pb2.ProductionRequest):
                                    ab_request.production.extend([request])
                                else:
                                    if isinstance(request, abathur_pb2.IntelRequest):
                                        ab_request.intel.CopyFrom(request)
                                    else:
                                        if isinstance(request, abathur_pb2.RawRequest):
                                            ab_request.raw.CopyFrom(request)
                                        else:
                                            if isinstance(request, abathur_pb2.RestartRequest):
                                                ab_request.restart.CopyFrom(request)
                        ab_request.only_async = self.only_async
                        self.man.send_to_c_sharp(ab_request)
                    else:
                        empty_ab = abathur_pb2.AbathurRequest()
                        empty_ab.only_async = self.only_async
                        self.man.send_to_c_sharp(empty_ab)

        except KeyboardInterrupt:
            print("Interrupted")
        except ConnectionAbortedError:
            pass
        except ConnectionResetError:
            pass
        finally:
            if self.man is not None:
                self.man.s.close()
            print("shut down main")

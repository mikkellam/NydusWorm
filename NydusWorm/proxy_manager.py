import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0, dir_path + "/protocol")
import sc2api_pb2
import abathur_pb2
import socket
import queue
import threading
timeout = 120


class ProxyManager:
    """Class managing the connection and transfer of data between Python and C#"""
    def __init__(self, port):
        self.host = "127.0.0.1"
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.msg_queue = queue.Queue()
        self.modules = []
        self.response_map = {}
        self.answers = queue.Queue()
        self.intel_received = threading.Event()

    def send_to_c_sharp(self, request):
        """takes a protobuf request and sends it to C#"""
        # Serialize Request and messagelength
        mess = request.SerializeToString()
        length = len(mess).to_bytes(4, "little")

        # Compose message in bytearray and send to c#
        msg = bytearray()
        msg.extend(length)
        msg.extend(mess)
        self.s.send(msg)

    def send_raw(self, request, want_answer=False):
        """
        Send a raw request rather than using the frameworks services
        :param request: A valid "Request" from sc2api_pb
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        ab_request = abathur_pb2.AbathurRequest()
        raw_req = abathur_pb2.RawRequest()
        raw_req.request.CopyFrom(request)
        raw_req.getResponse = want_answer
        ab_request.raw.CopyFrom(raw_req)
        if want_answer:
            event = threading.Event()
            self.response_map.update({raw_req.request.WhichOneof("request"): event})  #TODO the tabel will have values of type Event or Response is this ok??
        self.send_to_c_sharp(ab_request)
        if want_answer:
            if event.wait(timeout):
                return self.response_map[raw_req.request.WhichOneof("request")]
            print("timed out when waiting for raw response.")

    def send_quit(self, want_answer=False):
        """
        send a quit request to SC2 client
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.quit.CopyFrom(sc2api_pb2.RequestQuit())
        return self.send_raw(request, want_answer)

    def send_obs_req(self, want_answer=False):
        """
        request an observation from SC2
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.observation.CopyFrom(sc2api_pb2.RequestObservation())
        return self.send_raw(request, want_answer)

    def send_join_game(self, race, observer=0, want_answer=False):
        """
        send a join game request to SC2
        :param race: participant race
        :param observer:
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.join_game.CopyFrom(sc2api_pb2.RequestJoinGame())
        if race is not 0:
            request.join_game.race = race
        else:
            request.join_game.observer = observer
        return self.send_raw(request, want_answer)

    def send_restart(self, want_answer=False):
        """
        send a request to restart the game directly to SC2 (recommend using the restart_game function instead)
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.restart_game.CopyFrom(sc2api_pb2.RequestRestartGame())
        return self.send_raw(request, want_answer)

    def send_leave_game(self, want_answer=False):
        """
        send a request to leave the current game
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.leave_game.CopyFrom(sc2api_pb2.RequestLeaveGame())
        return self.send_raw(request, want_answer)

    def send_quick_save(self, want_answer=False):
        """
        send request to create a quicksave
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.quick_save.CopyFrom(sc2api_pb2.RequestQuickSave())
        return self.send_raw(request, want_answer)

    def send_quick_load(self, want_answer=False):
        """
        send a request to quickload
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.quick_load.CopyFrom(sc2api_pb2.RequestQuickLoad())
        return self.send_raw(request, want_answer)

    def send_game_info_req(self, want_answer=False):
        """
        Request to get the gameinfo from the SC2 client
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.game_info.CopyFrom(sc2api_pb2.RequestGameInfo())
        return self.send_raw(request, want_answer)

    def send_save_replay(self, want_answer=False):
        """
        send a request to save a replay
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.save_replay.CopyFrom(sc2api_pb2.RequestSaveReplay())
        return self.send_raw(request, want_answer)

    def send_available_maps_req(self, want_answer=False):
        """
        send a request to receive all your available maps
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.available_maps.CopyFrom(sc2api_pb2.RequestAvailableMaps())
        return self.send_raw(request, want_answer)

    def send_ping_req(self, want_answer=False):
        """
        send a request to ping the SC2 client
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.ping.CopyFrom(sc2api_pb2.RequestPing())
        return self.send_raw(request, want_answer)

    def send_step_req(self, count, want_answer=False):
        """
        send a request to step directly to SC2.
        :param count: amount of steps
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.step.CopyFrom(sc2api_pb2.RequestStep())
        request.step.count = count
        return self.send_raw(request, want_answer)

    def send_data_req(self, want_answer=False, want_ability=False, want_unit_type=False, want_upgrade=False, want_buff=False):
        """
        send a request to receive various static data
        :param want_answer: wait for the response to the Request?
        :param want_ability: receive data about all abilities
        :param want_unit_type: receive data about all UnitTypes
        :param want_upgrade: receive data about all upgrades
        :param want_buff: receive data about all buffs
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.data.CopyFrom(sc2api_pb2.RequestData())
        request.data.ability_id = want_ability
        request.data.unit_type_id = want_unit_type
        request.data.upgrade_id = want_upgrade
        request.data.buff_id = want_buff
        return self.send_raw(request, want_answer)

    # TODO test. If it is a relevant raw command.
    def send_create_game(self, player_setup, disable_fog, random_seed, realtime, battlenet_map_name= "", local_map_data=[], local_map_path ="", want_answer=False):
        """
        Send a request to create a game directly to SC2
        :param player_setup:
        :param disable_fog:
        :param random_seed:
        :param realtime:
        :param battlenet_map_name: Either give this or local_map_data and local_map_path
        :param local_map_data:
        :param local_map_path:
        :param want_answer: wait for the response to the Request?
        :return: None or Response
        """
        request = sc2api_pb2.Request()
        request.create_game.CopyFrom(sc2api_pb2.RequestCreateGame())
        if battlenet_map_name is "":
            local_map = sc2api_pb2.LocalMap()
            local_map.map_path = local_map_path
            local_map.map_data = local_map_data
            request.create_game.local_map = local_map
        else:
            request.create_game.battlenet_map_name = battlenet_map_name
        request.create_game.player_setup = player_setup
        request.create_game.disable_fog = disable_fog
        request.create_game.random_seed = random_seed
        request.create_game.realtime = realtime
        return self.send_raw(request, want_answer)

    def add_module(self, module):
        """
        Add a module to the gameloop allowing it to receive callbacks
        :param module: A module implementing IModule or IAsyncModule
        :return: None
        """
        self.modules.append(module)

    def remove_module(self, module):
        """
        remove a module from the game loop. Making sure it will no longer receive callbacks
        :param module: A Module currently in the gameloop
        :return: None
        """
        self.modules.remove(module)

    def restart_game(self):
        """Make the framework restart the game"""
        self.answers.put(abathur_pb2.RestartRequest())

    def receive(self):
        """Listen for incoming messages from C#. return rawResponses to the calling methods
            and make the main thread handle the rest by putting them in the message queue"""
        try:
            while True:
                rec = self.s.recv(4)
                size = int.from_bytes(rec, "little")
                answ = bytearray()

                while size > 0:
                    chunk = self.s.recv(size)
                    answ.extend(chunk)
                    size -= len(chunk)
                response = abathur_pb2.AbathurResponse()
                response.ParseFromString(answ)
                if response.HasField("rawResponse"):
                    ev = self.response_map[response.rawResponse.WhichOneof("response")]
                    self.response_map.update({response.rawResponse.WhichOneof("response"): response})
                    ev.set()
                else:
                    self.msg_queue.put(response)

        except ConnectionAbortedError:
            print("Connection to Abathur aborted. Shutting down NydusWorm")
        except ConnectionResetError:
            print("Connection to Abathur was terminated. Shutting down NydusWorm")




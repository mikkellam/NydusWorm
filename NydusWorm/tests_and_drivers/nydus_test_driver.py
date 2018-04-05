import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.insert(0,dir_path + "/../protocol")
sys.path.insert(0,dir_path + "/..")
import abathur_pb2
import sc2api_pb2
import socket
import threading
import queue
import time

s = socket.socket()
host = "127.0.0.1"
port = 4008
s.bind((host, port))
hardcoded = queue.Queue()

def make_abathur(resp):
    ab_resp = abathur_pb2.AbathurResponse()
    ab_resp.rawResponse.CopyFrom(resp)
    return ab_resp

def hard_code():
    join = sc2api_pb2.Response()
    join.join_game.CopyFrom(sc2api_pb2.ResponseJoinGame())
    obs = sc2api_pb2.Response()
    obs.observation.CopyFrom(sc2api_pb2.ResponseObservation())
    restart = sc2api_pb2.Response()
    restart.restart_game.CopyFrom(sc2api_pb2.ResponseRestartGame())
    ping = sc2api_pb2.Response()
    ping.ping.CopyFrom(sc2api_pb2.ResponsePing())
    quit = sc2api_pb2.Response()
    quit.quit.CopyFrom(sc2api_pb2.ResponseQuit())
    leave = sc2api_pb2.Response()
    leave.leave_game.CopyFrom(sc2api_pb2.ResponseLeaveGame())
    data = sc2api_pb2.Response()
    data.data.CopyFrom(sc2api_pb2.ResponseData())
    #create = sc2api_pb2.Response()
    #create.create_game = sc2api_pb2.ResponseCreateGame()
    hardcoded.put(make_abathur(obs))
    hardcoded.put(make_abathur(quit))
    hardcoded.put(make_abathur(join))
    hardcoded.put(make_abathur(restart))
    hardcoded.put(make_abathur(data))
    hardcoded.put(make_abathur(ping))


hard_code()

try:
    s.listen(5)
    c = None


    def receive(conn):
        while True:
            time.sleep(2)
            size = int.from_bytes(conn.recv(4), "little")
            answ = bytearray()
            while size > 0:
                chunk = conn.recv(size)
                answ.extend(chunk)
                size -= len(chunk)

            request = abathur_pb2.AbathurRequest()
            request.ParseFromString(answ)

            ab_resp = abathur_pb2.AbathurResponse()
            notifi = abathur_pb2.Notification()
            notifi.type = abathur_pb2.GameStep
            ab_resp.notification.CopyFrom(notifi)

            # Serialize Request and messagelength
            response = ab_resp
            mess = response.SerializeToString()
            length = len(mess).to_bytes(4, "little")
            print(request)

            # Compose message in bytearray and send to c#
            msg = bytearray()
            msg.extend(length)
            msg.extend(mess)
            print(response)
            conn.send(msg)

    if c is None:
        # Halts
        print('[Waiting for connection...]')
        c, addr = s.accept()
        print('Got connection from', addr)

    t = threading.Thread(target=receive, args=(c,))
    t.start()

    while True:
        pass# Halts
        #q = input("Enter something to this client: ")
        #c.send(q.encode())

except KeyboardInterrupt:
    print("Interrupted")

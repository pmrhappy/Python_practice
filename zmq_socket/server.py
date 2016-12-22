import zmq
import sys

'''context=zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:6757")
msg=socket.recv()
IpcPort="5598"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:"+IpcPort)
msg_filter = "PHM"      
#zip_filter = zip_filter.decode('ascii')
#socket.setsockopt_string(zmq.REP, msg_filter)   

while True:
    msg=input()
    socket.send(9)'''
c=25

context = zmq.Context()

socket = context.socket(zmq.PUB)
socket.bind ("tcp://127.0.0.1:5568")

while True:
    #msg=socket.recv()
    #print(msg)
    reply = input("reply:")
    socket.send_string(reply)


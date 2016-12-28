import zmq

'''context=zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:6757")
msg=socket.recv()
IpcPort="5598"
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:"+IpcPort)
msg_filter = "PHM"      
#zip_filter = zip_filter.decode('ascii')
#socket.setsockopt_string(zmq.SUBSCRIBE, msg_filter)   

while True:
    msg = socket.recv()
    print(msg)
    input()'''


context = zmq.Context()

socket = context.socket(zmq.SUB)
socket.connect ("tcp://127.0.0.1:5566")
topicfilter = ""
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)


while True:
    if poller.poll(2*1000): # 10s timeout in milliseconds
        msg = socket.recv_string()
        print (msg)
    else:
        print("waiting for message...")
    

    
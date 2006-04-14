import threading
import socket
import system
import utils
import select
import Queue
import pickle

class ChatSockets(threading.Thread):

    def __init__(self,puttowidget):
        ##### settingup the server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind( (socket.getfqdn(), system.listenport) )
        self.server.listen(5)
        self.server.setblocking(0)

        self.puttowidget = puttowidget
        self.socklist = [self.server]
        self.keeplistening = True
        self.queue = Queue.Queue(0)

        threading.Thread.__init__(self)

    def run(self):

        class Worker(threading.Thread):

            def __init__(self, queue):
                self.queue = queue
                self.keepworking = True
                threading.Thread.__init__(self)
            def run(self):
                while self.keepworking:
                    try:
                        (do,sock) = self.queue.get(True,system.queuetimeout)
                        do(sock)
                    except Queue.Empty:
                        pass
            def die(self):
                self.keepworking = False

        self.w = list()
        for i in range(0,system.workers):
            worker = Worker(self.queue)
            worker.start()
            self.w.append(worker)

        while self.keeplistening:
            (sread, swrite, sexc) = select.select( self.socklist, [], [], system.selecttimeout )
            if sread:
                for sock in sread:
                    if sock == self.server:
                        newsock, (remhost, remport) = sock.accept()
                        self.queue.put( (self.addConnection, newsock) )
                    else:
                        self.socklist.remove(sock)
                        self.queue.put( (self.manageMsg, sock) )

    def die(self):
        self.keeplistening = False
        for worker in self.w:
            worker.die()
        for worker in self.w:
            worker.join()

    def addConnection(self,sock):
        self.socklist.append(sock)
        print " ...connection OK."

    def manageMsg(self,sock):
        msg = self.getMsg(sock)
        self.broadcastMsg(msg,sock)
        self.socklist.append(sock)

    def sendMsg(self,msg,sock):
        sock.sendall(msg)

    def broadcastMsg(self,msg,omit=None):
        msglen = str(len(msg)).ljust(system.msglensize)
        msg = msglen + msg
        for sock in self.socklist:
            if not ( (sock == self.server) or (sock == omit) ):
                self.sendMsg(msg,sock)

    def getMsg(self,sock):
        msgsize = ""
        recived = 0
        while recived < system.msglensize:
            msgsize += sock.recv(system.msglensize - recived)
            recived = len(msgsize)
        msgsize = int(msgsize)

        recived = 0
        msg = ""
        while recived < msgsize:
            msg += sock.recv(msgsize - recived)
            recived = len(msg)
        print msg

        return msg

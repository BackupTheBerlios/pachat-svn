#####   PAchat, a nice chat program
#####   Copyright (C) 2006 Banesiu Sever <raperu2000@yahoo.com>

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

##############################################################################

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
        freeportfound = False
        while not freeportfound:
            try:
                self.server.bind( (socket.getfqdn(), system.listenport) )
                self.server.listen(5)
                self.socklist = [self.server]
                self.fullsocklist = []
                freeportfound = True
                print "listening on port " + str(system.listenport)
            except socket.error:
                system.listenport += 1

        self.puttowidget = puttowidget
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

    def killThreads(self):
        self.keeplistening = False
        for worker in self.w:
            worker.die()
        for worker in self.w:
            worker.join()

    def addConnection(self,sock):
        print "addConection"
        self.socklist.append(sock)
        self.fullsocklist.append(sock)
        print " ...connection OK."

    def manageMsg(self,sock):
        msg = self.getMsg(sock)
        if not msg:
            ##### exiting
            print "Nice exit!"
            self.fullsocklist.remove(sock)
            return
        self.broadcastMsg(msg,sock)
        self.socklist.append(sock)

    def sendMsg(self,msg,sock):
        try:
            sock.sendall(msg)
        except socket.error:
            print "send error"
            pass

    def broadcastMsg(self,msg,omit=False):
        msglen = str(len(msg)).ljust(system.msglensize)
        msg = msglen + msg
        for sock in self.fullsocklist:
            if not (sock == omit):
                self.sendMsg(msg,sock)

    def getMsg(self,sock):

        import time
        msgsize = ""
        lastrecived = 0
        recived = 0
        while recived < system.msglensize:
            try:
                msgsize += sock.recv(system.msglensize - recived)
            except socket.error:
                print "socket error"
                return
            recived = len(msgsize)
            if recived == lastrecived:
                if recived == 0:
                    print "recived 0"
                else:
                    print "stopped"
                return
            lastrecived = recived

        msgsize = int(msgsize)
        recived = 0
        lastrecived
        msg = ""
        while recived < msgsize:
            try:
                msg += sock.recv(msgsize - recived)
                time.sleep(2)
                print "pause"
            except socket.error:
                print "socket error msg"
                return
            recived = len(msg)
            if recived == lastrecived:
                if recived == 0:
                    print "recived 0 in msg"
                else:
                    print "stopped in msg"
                return
        print "*"
##        utils.putMsg(self.puttowidget,msg)
        return msg

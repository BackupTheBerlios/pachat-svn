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

import utils
import system

##############################################################################

def clear(GUIobj,arglist=None):
    from Tkinter import END
    widget = GUIobj.chat_window
    utils.keepStateAndDo(widget, widget.delete, "0.0", widget.index(END) )

##############################################################################

def nick(GUIobj,arglist=None):
    if not arglist:
        msg = system.msg["nick"]["nonick"]
    else:
        system.usernick = arglist[0]
        msg = system.msg["nick"]["changed"].replace("{nick}", arglist[0])
    utils.putMsg( GUIobj.chat_window , msg )

##############################################################################

def quitgui(GUIobj,arglist=None):
##    GUIobj.chatsockets.killThreads()
##    GUIobj.chatsockets.join()
    GUIobj.root.destroy()

##############################################################################

def connect(GUIobj,arglist=None):
    if not arglist:
        utils.putMsg(GUIobj.chat_window, system.msg["connect"]["noip"])
        return
    port = system.connport
    ipport = arglist[0].split(":",1)
    ip = ipport[0]
    if len(ipport) > 1:
        try:
            port = int(ipport[1])
        except ValueError:
            msg = system.msg["connect"]["badport"].replace("{badport}",ipport[1])
            utils.putMsg( GUIobj.chat_window, msg )
            return
    import threading
    import socket
    class Con(threading.Thread):
        def __init__(self,call):
            self.call = call
            threading.Thread.__init__(self)
        def run(self):
            try:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.connect((ip,port))
                self.call(sock)
            except socket.error:
                print "conn timedout"
    c = Con(GUIobj.chatsockets.addConnection)
    c.start()

##############################################################################

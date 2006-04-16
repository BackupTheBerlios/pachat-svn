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

import system

##############################################################################

def putMsg(widget,msg):
    from Tkinter import END
    if not msg: return
    keepStateAndDo( widget, widget.insert, widget.index(END), msg+"\n")
    widget.see(widget.index(END))

##############################################################################

def keepStateAndDo(widget,action,*args):
    restate = 0
    if widget["state"] == "disabled":
        widget["state"] = "normal"
        restate = 1
    action(*args)
    if restate:
        widget["state"] = "disabled"

##############################################################################

def makeNick(nick):
    return system.ltag + nick + system.rtag

##############################################################################

def doCommand(GUIobj,command):
    import commandsconf
    command = command.split()
    for cmd,dowhat in commandsconf.com.items():
        cmd_found = False
        if cmd == command[0]:
            cmd_found = True
            if type(dowhat) is list:
                for dothis in dowhat:
                    dothis(GUIobj,command[1:])
            else:
                dowhat(GUIobj,command[1:])
            break
    if not cmd_found:
        putMsg(GUIobj.chat_window, system.msg["err"]["badcmd"].replace("{badcmd}",command[0]))

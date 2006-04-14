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
import utils

##############################################################################

def doScroll(event,GUIobj,*args):
    """ make the scroll scrolling :)
    """

    widget = GUIobj.chat_window
    op, howMany = args[0], args[1]
    if op == "scroll":
        units  =  args[2]
        widget.yview_scroll ( howMany, units )
    elif op == "moveto":
        widget.yview_moveto ( howMany )

##############################################################################

def doInfo(event,GUIobj):
    """ open the browser at the given url
    """
    import webbrowser

    url = system.url
    try:
        webbrowser.open(url)
    except ImportError: # pre-webbrowser.py compatibility
        import sys
        import os
        if sys.platform == 'win32':
            os.system('start "%s"' % url)
        elif sys.platform == 'mac':
            try: import ic
            except ImportError: pass
            else: ic.launchurl(url)
        else:
            rc = os.system('netscape -remote "openURL(%s)" &' % url)
            if rc: os.system('netscape "%s" &' % url)

##############################################################################

def sendMsg(event,GUIobj):
    """ print the message in chatwindow and execute commands
    """
    from Tkinter import END

    widget = event.widget
    msg = widget.get()
    widget.delete(0,widget.index(END))
    lines = msg.split("\n")
    for line in lines:
        strip_line = line.strip()
        if strip_line[0:1] == "/":
            utils.doCommand(GUIobj,strip_line[1:])
            return
        else:
            plain_msg = line.rstrip()
            if len(plain_msg) > system.msglength:
                plain_msg = system.msg["err"]["msglen"].replace("{msglen}",str(system.msglength))
                utils.putMsg(GUIobj.chat_window, plain_msg)
                return
        nick = utils.makeNick(system.usernick)
        plain_msg = nick + plain_msg
        GUIobj.chatsockets.broadcastMsg(plain_msg)
        utils.putMsg(GUIobj.chat_window, plain_msg)    

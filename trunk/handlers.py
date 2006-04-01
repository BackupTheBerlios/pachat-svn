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

import systemconfig
import utils

##############################################################################

def doScroll(event,GUIobj,*args):
    """ make the scroll scrolling :)
    """

    widget = GUIobj.getChatWindow()
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

    url = systemconfig.url

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
    from commandsconfigaccess import extractCommands

    widget = event.widget
    msg = widget.get()
    msg = extractCommands(GUIobj,msg)
    widget.delete(0,widget.index(END))
    if not msg:
        return

    for m in msg:
        m = m.rstrip()
        if len(m) > systemconfig.msglength:
            m = systemconfig.err01
        else:
            nick = utils.makeNick(systemconfig.usernick)
            m = nick + m
        utils.putMsg( GUIobj.getChatWindow(), m)

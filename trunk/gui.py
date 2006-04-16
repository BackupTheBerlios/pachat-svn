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

from Tkinter import *

class GUI:
    """ GUI class
    """
    def __init__(self, parent):
        self.root = parent

    def makeGUI(self):
        """ rendering and binding a simple GUI
        """

        from guiconf import GUIConf as gui_config
        import handlersconf as handlers_config

        ##### top banner (label)
        self.banner = Label(self.root)
        self._renderWidget( self.banner, gui_config.banner )
        self._doBindings( self.banner, handlers_config.banner )

        ##### chat window (text)
        self.chat_window = Text(self.root)
        self._renderWidget( self.chat_window, gui_config.chat_window )

        ##### chat widnow scroll (scrollbar)
        ##### this is the way we bind commands; nice, right?
        self.chat_scroll = Scrollbar(self.root, command=lambda *args:
                                                 self._commandHandler( handlers_config.chat_scroll, *args ) )

        self._renderWidget( self.chat_scroll, gui_config.chat_scroll )
        self.chat_window["yscrollcommand"] = self.chat_scroll.set

        ##### input area (entry)
        self.input_area = Entry(self.root)
        self._renderWidget( self.input_area, gui_config.input_area )
        self.input_area.focus_force()
        self._doBindings( self.input_area, handlers_config.input_area )

        ##### sockets
        import chatsockets
        self.chatsockets = chatsockets.ChatSockets(self.chat_window)
        self.chatsockets.start()

        ##### startup script
        from startup import doStartup
        self.startup = doStartup(self)

    def _doBindings(self,widget,ehlist):
        """ binding events to handlers configured in ehlist
        """
        for eh in ehlist:
            ev,ha = eh
            if eh != "command":
                widget.bind(ev, lambda event, arg1 = ev, arg2 = ehlist: self._eventHandler(event, arg1, arg2) )

    def _eventHandler(self,event,e,ehlist,*args):
        """ just calling the needed handlers and passing the arguments
        """
        for eh in ehlist:
            ev,ha = eh
            if ev == e:
                ha(event,self,*args)

    def _commandHandler(self,ehlist,*args):
        """ this can be done using directly _eventHandler but is easyer this way
        """
        self._eventHandler(None,"command",ehlist,*args)

    def _renderWidget(self,widget,makeup):
        """ rendering the widget with the options passed in makeup
        """
        config,grid = makeup
        for key,value in config.items():
            widget[key] = value
        if grid:
            widget.grid(
                column      = grid["column"],
                columnspan  = grid["columnspan"],
                in_         = grid["in"],
                ipadx       = grid["ipadx"],
                ipady       = grid["ipady"],
                padx        = grid["padx"],
                pady        = grid["pady"],
                row         = grid["row"],
                rowspan     = grid["rowspan"],
                sticky      = grid["sticky"]
            )
        else:
            widget.grid()

    def __del__(self):
        self.chatsockets.killThreads()
        self.chatsockets.join()

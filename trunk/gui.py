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

        import chatconfigaccess as chat_config
        import bindingsconfigaccess as bindings_config

        ##### top banner (label)
        self.banner = Label(self.root)
        self._renderWidget( self.banner, chat_config.getBanner() )
        self._doBindings( self.banner, bindings_config.getBanner() )

        ##### chat window (text)
        self.chat_window = Text(self.root)
        self._renderWidget( self.chat_window, chat_config.getChatWindow() )

        ##### chat widnow scroll (scrollbar)
        ##### this is the way we bind command; nice, right?
        self.chat_scroll = Scrollbar(self.root, command=lambda *args:
                                                 self._commandHandler( bindings_config.getChatScroll(), *args ) )

        self._renderWidget( self.chat_scroll, chat_config.getChatScroll() )
        self.chat_window["yscrollcommand"] = self.chat_scroll.set

        ##### input area (entry)
        self.input_area = Entry(self.root)
        self._renderWidget( self.input_area, chat_config.getInputArea() )
        self.input_area.focus_force()
        self._doBindings( self.input_area, bindings_config.getInputArea() )

        ##### startup script
        from startup import doStartup
        doStartup(self)

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

    ##### access functions, nothing fancy
    def getBanner(self):
        return self.banner

    def getChatWindow(self):
        return self.chat_window

    def getChatScroll(self):
        return self.chat_scroll

    def getInputArea(self):
        return self.input_area

##### main program
def run():
    """ starting the interface
    """
    root = Tk()
    root.columnconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)

    gui = GUI(root)
    gui.makeGUI()

    root.mainloop()

if __name__ == "__main__":
    run()

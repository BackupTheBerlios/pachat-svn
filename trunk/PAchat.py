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

##### main program
def run():
    """ starting the interface
    """

    from gui import GUI
    from Tkinter import Tk
    import system

    root = Tk()
    root.columnconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.title(system.name + " " + system.version)
    root.minsize(width= system.minwidth , height=system.minheight)
    root.geometry(system.defsize)

    gui = GUI(root)
    gui.makeGUI()

    root.mainloop()

if __name__ == "__main__":
    run()

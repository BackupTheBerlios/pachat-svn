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

##### top banner (label)
b                           = dict()
b["text"]                   = systemconfig.name + " " + systemconfig.version
b["foreground"]             = "blue"
b["cursor"]                 = "hand2"
b["grid"]                   = dict()
b["grid"]["row"]            = 0
b["grid"]["column"]         = 0
b["grid"]["columnspan"]     = 2
b["grid"]["sticky"]         = None

##### chat window (text)
c                           = dict()
c["background"]             = "white"
c["selectbackground"]       = "#000"
c["selectforeground"]       = "#FFF"
c["font"]                   = ("Courier",10)
c["selectborderwidth"]      = 0
c["takefocus"]              = -1
c["padx"]                   = 5
c["pady"]                   = 5
c["spacing3"]               = 5
c["state"]                  = "disabled"
c["relief"]                 = "flat"
c["grid"]                   = dict()
c["grid"]["row"]            = 1
c["grid"]["column"]         = 0
c["grid"]["sticky"]         = "w e s n"

##### chat widnow scroll (scrollbar)
cs                          = dict()
cs["orient"]                = "vertical"
cs["takefocus"]             = -1
cs["grid"]                  = dict()
cs["grid"]["row"]           = 1
cs["grid"]["column"]        = 1
cs["grid"]["sticky"]        = "s n"

##### input area (entry)
i                           = dict()
i["background"]             = "#333"
i["foreground"]             = "#FFF"
i["highlightthickness"]     = 2
i["highlightcolor"]         = "#000"
i["highlightbackground"]    = "#777"
i["insertbackground"]       = "#FFF"
i["selectbackground"]       = "#FFF"
i["selectforeground"]       = "#000"
i["relief"]                 = "flat"
i["font"]                   = ("Courier",10)
i["selectborderwidth"]      = 0
i["grid"]                   = dict()
i["grid"]["row"]            = 2
i["grid"]["column"]         = 0
i["grid"]["columnspan"]     = 2
i["grid"]["sticky"]         = "w e"

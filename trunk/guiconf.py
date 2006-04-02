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

class _conf:
    ##### top banner (label)
    b                           = dict()
    b["text"]                   = system.name + " " + system.version
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
    c["font"]                   = ("Verdana",9)
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
    i["font"]                   = ("Verdana",9)
    i["selectborderwidth"]      = 0
    i["grid"]                   = dict()
    i["grid"]["row"]            = 2
    i["grid"]["column"]         = 0
    i["grid"]["columnspan"]     = 2
    i["grid"]["sticky"]         = "w e"

##### do not edit from here
class _GUIConf:
    """ guiconfig access
    """
    def __getattr__(self, name):
        if      name == "banner":
            return self._getValues(_conf.b)
        elif    name == "chat_window":
            return self._getValues(_conf.c)
        elif    name == "chat_scroll":
            return self._getValues(_conf.cs)
        elif    name == "input_area":
            return self._getValues(_conf.i)
        else:
            raise AttributeError, name

    def __setattr__(self, name, value):
        pass

    def _getValues(self,var):
        if not var.has_key("grid"):
            return (var,None)
        else:
            if var["grid"]:
                for key in ("column","columnspan","in","ipadx","ipady","padx","pady","row","rowspan","sticky"):
                    if not var["grid"].has_key(key):
                        var["grid"][key] = None
            tmp_var = var.copy()
            grid = tmp_var["grid"]
            del tmp_var["grid"]
            return (tmp_var,grid)

GUIConf = _GUIConf()

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

import chatconfig

def getBanner():
    return _getValues(chatconfig.b)

def getChatWindow():
    return _getValues(chatconfig.c)

def getChatScroll():
    return _getValues(chatconfig.cs)

def getInputArea():
    return _getValues(chatconfig.i)

def _getValues(var):

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

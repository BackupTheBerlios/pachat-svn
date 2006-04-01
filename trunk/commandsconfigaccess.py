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

import commandsconfig as cc

##############################################################################

def extractCommands(GUIobj,com):
    command = com.split("\n")
    tmp_cmd = command[:]

    for c in command:
        cs = c.strip()
        if cs[0:1] == "/":
            doCommand(GUIobj,cs[1:])
            tmp_cmd.remove(c)
    return tmp_cmd

def doCommand(GUIobj,command):
    command = command.split()
    for cmd,dowhat in cc.com.items():
        if cmd == command[0]:
            try:
                for dothis in dowhat:
                    dothis(GUIobj,command[1:])
            except TypeError:
                dowhat(GUIobj,command[1:])

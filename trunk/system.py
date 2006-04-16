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

##### system wide settings
name            = "PAchat"
usernick        = "PAc"
sysnick         = "System"
ltag            = "["
rtag            = "]: "
version         = "v0.1"
bannercolor     = "blue"
firstmsg        = name + " " + version + "\nHi!\nType /help for help."
url             = "http://developer.berlios.de/projects/pachat/"
msglength       = 1020
minwidth        = 300
minheight       = 200
defsize         = "400x350"
listenport      = 7777
connport        = 7777
msglensize      = 10

##### sockets and threading
workers         = 2
queuetimeout    = 1
selecttimeout   = 0.2

##### program msgs
msg                     = dict()

##### general error msg
msg["err"]              = dict()
msg["err"]["msglen"]    = "Message way to long! Max length is {msglen}."
msg["err"]["badcmd"]    = "Unknown command {badcmd}."

##### cmd msgs
msg["nick"]                 = dict()
msg["nick"]["nonick"]       = "No nick given."
msg["nick"]["changed"]      = "New nick is {nick}."
msg["connect"]              = dict()
msg["connect"]["noip"]      = "No ip/hostname given."
msg["connect"]["badport"]   = "Bad port {badport}."

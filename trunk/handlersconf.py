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

import handlers

##### This way you can call a function with a predefined argument
#####    ("<Enter>",lambda *args: handlers.doSomething("arg1", "arg2..." ,*args) )
##### You cand bind a single action to multiple handlers

##### top banner (label)
banner      = [("<Button-1>",handlers.doInfo)]

##### input area (entry)
input_area       = [("<Return>",handlers.sendMsg)]

##### chat widnow scroll (scrollbar)
chat_scroll      = [("command",handlers.doScroll)]

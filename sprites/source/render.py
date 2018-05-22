#!/usr/bin/env python
"""
Towering: Tower defence game.
Copyright (C) 2018 Ghostkeeper
This game is free software: You can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This game is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
You should have received a copy of the GNU Affero General Public License along with this game. If not, see <https://gnu.org/licenses/>.
"""

"""
This script converts all SVG files in the folder to PNG.
It depends on Inkscape being installed on your system.
"""

import os
import os.path
import subprocess

possible_inkscape_executables = [
	"C:\\Program Files (x86)\\Inkscape\\inkscape.exe",
	"C:\\Program Files\\Inkscape\\inkscape.exe",
	"inkscape" #Unix.
]

for filename in os.listdir(os.getcwd()):
	base, extension = os.path.splitext(filename)
	if(extension != ".svg"):
		continue
	new_filename = os.path.join(os.getcwd(), "..", base + ".png")
	print(new_filename)
	for executable in possible_inkscape_executables:
		try:
			subprocess.run([executable, "-z", "-e", new_filename, filename])
			break
		except Exception as e:
			pass #Probably wrong operating system.
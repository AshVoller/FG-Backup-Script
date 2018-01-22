#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FG-Backup-Script.py
#  
#  Copyright 2018 Vince Winter <vwinter@freekbox>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os


def main():
	if os.path.exists("/etc/os-release"):
		import fg-linux
		return 0
	elif os.path.exists("/Volumes/"):
		import fg-mac
		return 0
	elif os.path.exists("/Documents and Settings"):
		import fg-mac
		return 0
	else:
		import fg-fallback
	return 0

if __name__ == '__main__':
	main()


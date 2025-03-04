#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 ~ 2015 Deepin, Inc.
#               2011 ~ 2015 Wang YaoHua
#
# Author:     Wang YaoHua <mr.asianwang@gmail.com>
# Maintainer: Wang YaoHua <mr.asianwang@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

dirname = os.path.dirname
abspath = os.path.abspath

MAIN_DIR = dirname(dirname(abspath(__file__)))
MAIN_QML = os.path.join(dirname(abspath(__file__)), "Main.qml")
OSD_QML = os.path.join(dirname(abspath(__file__)), "OSD.qml")
GTK_CLIP = os.path.join(MAIN_DIR, "src/gtk-clip")

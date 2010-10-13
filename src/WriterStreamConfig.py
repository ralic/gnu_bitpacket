#!/usr/bin/env python
#
# @file    WriterStreamConfig.py
# @brief   Configuration parameters for stream writers
# @author  Aleix Conchillo Flaque <aleix@member.fsf.org>
# @date    Fri Mar 12, 2010 15:08
#
# Copyright (C) 2010 Aleix Conchillo Flaque
#
# This file is part of BitPacket.
#
# BitPacket is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BitPacket is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BitPacket.  If not, see <http://www.gnu.org/licenses/>.
#

__doc__ = '''

    **API reference**: :class:`WriterStreamConfig`

'''

from utils.string import u_str

from WriterConfig import WriterConfig

__DEFAULT_INDENTATION__ = 2
__DEFAULT_NEWLINE__ = u_str("\n")

class WriterStreamConfig(WriterConfig):

    def __init__(self, config = {}):
        self.indentation = __DEFAULT_INDENTATION__
        self.newline = __DEFAULT_NEWLINE__
        WriterConfig.__init__(self, config)

#!/usr/bin/env python
#
# @file    WriterTable.py
# @brief   An object-oriented representation of bit field structures
# @author  Aleix Conchillo Flaque <aleix@member.fsf.org>
# @date    Wed Aug 05, 2009 17:37
#
# Copyright (C) 2007-2009 Aleix Conchillo Flaque
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

from utils.string import wrap_string

from Writer import Writer


__TABLE_NAME_SIZE__ = 25
__TABLE_TYPE_SIZE__ = 8
__TABLE_HEX_SIZE__ = 25
__TABLE_STR_SIZE__ = 25


class WriterTable(Writer):

    def start_block(self, field):
        name_size = __TABLE_NAME_SIZE__ - len(self.indentation())
        s = '| ' + Writer.start_block(self, field)
        s += '%-*s | %4d %-4s | %*s | %*s | %*s |' \
            % (name_size,
               wrap_string(field.name(), name_size),
               field.size(), field.type(),
               __TABLE_HEX_SIZE__, '',
               __TABLE_STR_SIZE__, '',
               __TABLE_STR_SIZE__, '')
        return s

    def write(self, field):
        name_size = __TABLE_NAME_SIZE__ - len(self.indentation())
        s = '| ' + self.indentation()
        s += '%-*s | %4d %-4s | %*s | %*s | %*s |' \
            % (name_size,
               wrap_string(field.name(), name_size),
               field.size(), field.type(),
               __TABLE_HEX_SIZE__,
               wrap_string(field.str_hex_value(), __TABLE_HEX_SIZE__),
               __TABLE_STR_SIZE__,
               wrap_string(field.str_value(), __TABLE_STR_SIZE__),
               __TABLE_STR_SIZE__,
               wrap_string(field.str_eng_value(), __TABLE_STR_SIZE__))
        return s

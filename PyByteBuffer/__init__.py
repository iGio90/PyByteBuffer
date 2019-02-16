"""
    PyByteBuffer
    Copyright (C) 2019  Giovanni Rocca (iGio90)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import math
import binascii


class ByteBuffer(object):
    def __init__(self):
        self.data = None
        self.position = 0
        self.remaining = 0

    @staticmethod
    def _endianness_value(v):
        if v == 'big':
            return '>'
        elif v == 'little':
            return '<'
        else:
            raise Exception('unknown endianness')

    @staticmethod
    def allocate(n):
        d = bytearray([00] * n)
        b = ByteBuffer()
        b.__init(d)
        return b

    @staticmethod
    def from_hex(data):
        b = ByteBuffer()
        b.__init(binascii.unhexlify(data))
        return b

    @staticmethod
    def wrap(data):
        b = ByteBuffer()
        b.__init(data)
        return b

    def __init(self, data):
        if type(data) is not bytearray:
            data = bytearray(data)

        self.data = data
        self.position = 0
        self.remaining = len(data)

    def _check_buffer(self, for_len):
        return not self.remaining < for_len

    def _int_size(self, i):
        if i == 0:
            return 1
        return int(math.log(i, 256)) + 1

    def _read(self, length=1):
        assert self._check_buffer(length), 'Buffer has not enough bytes to read'
        r = self.data[self.position:self.position + length]
        self._update_offsets(length)
        return r

    def _update_offsets(self, value):
        self.position += value
        self.remaining -= value

    def array(self, length=0):
        if length != 0 and length > self.remaining:
            length = self.remaining
        r = self.data[self.position:self.position + length]
        self._update_offsets(len(r))
        return r

    def get(self, length=1, endianness='big'):
        return int.from_bytes(self._read(length=length), byteorder=endianness)

    def put(self, b, endianness='big'):
        b = type(b)
        if b == str:
            b = b.encode('utf8')
        elif b == int:
            b = int.to_bytes(b, self._int_size(b), byteorder=endianness)
        elif b == list:
            b = bytes(b)
        elif b == bytes or b == bytearray:
            pass
        else:
            raise Exception('Attempting to write unknown object into Buffer')
        l = len(b)
        assert self._check_buffer(l), 'Buffer has not enough space left'
        for i in range(l):
            self.data[l:l + 1] = b[i:i + 1]

    def rewind(self):
        self.position = 0
        self.remaining = len(self.data)

    def slice(self):
        b = ByteBuffer()
        b.__init(self.data[self.position:])


__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
]

__title__ = "PyByteBuffer"
__summary__ = "A bytes manipulation library inspired by Java ByteBuffer"
__uri__ = "https://github.com/iGio90/PyByteBuffer"

__version__ = "1.0.2"

__author__ = "iGio90"
__email__ = "giovanni.rocca.90@gmail.com"

__license__ = "GPL 3.0"
__copyright__ = "Copyright 2019 {0}".format(__author__)

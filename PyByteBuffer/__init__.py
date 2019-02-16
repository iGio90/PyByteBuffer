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
    def allocate(n):
        """
        :param n: size of allocation
        :return: a ByteBuffer object wrapping an empty buffer of size n
        """
        d = bytearray([00] * n)
        b = ByteBuffer()
        b.__init(d)
        return b

    @staticmethod
    def from_hex(hex_str):
        """
        :param hex_str: an hexadecimal string
        :return: a ByteBuffer object wrapping a buffer decoded from hex_str
        """
        b = ByteBuffer()
        b.__init(binascii.unhexlify(hex_str))
        return b

    @staticmethod
    def wrap(data):
        """
        :param data: a bytes/bytearray object
        :return: a ByteBuffer object wrapping a the data provided
        """
        b = ByteBuffer()
        b.__init(data)
        return b

    def __init(self, data):
        """
        Initialize this buffer with the given data
        :param data:
        :return:
        """
        if type(data) is not bytearray:
            data = bytearray(data)

        self.data = data
        self.position = 0
        self.remaining = len(data)

    def _check_buffer(self, for_len):
        """
        :param for_len: the length to check
        :return: whether if this buffer has enough space left for r/w op
        """
        return not self.remaining < for_len

    def _int_size(self, i):
        """
        :param i: an int object
        :return: the number of bytes of the given int
        """
        if i == 0:
            return 1
        return int(math.log(i, 256)) + 1

    def _read(self, length=1):
        """
        for internal usage, read length byte from the source and update position
        :param length: the number of bytes to read
        :return: a bytearray object of the required size starting from current position
        """
        assert self._check_buffer(length), 'Buffer has not enough bytes to read'
        r = self.data[self.position:self.position + length]
        self._update_offsets(length)
        return r

    def _update_offsets(self, value):
        """
        update the position of this buffer
        :param value: the number of bytes for the increment
        :return:
        """
        self.position += value
        self.remaining -= value

    def array(self, length=0):
        """
        get a bytearray object and increment position
        :param length: the number of bytes required or 0/not provided for the remaining bytes
        :return: a bytearray object of the required length
        """
        if length != 0 and length > self.remaining:
            length = self.remaining
        r = self.data[self.position:self.position + length]
        self._update_offsets(len(r))
        return r

    def get(self, length=1, endianness='big'):
        """
        get an int object and increment position
        :param length: an optional bytes length. default: 1
        :param endianness: the byte order. default: big
        :return: the int representation of requested bytes
        """
        return int.from_bytes(self._read(length=length), byteorder=endianness)

    def put(self, b, endianness='big'):
        """
        write data in the buffer and increment position
        :param b: the data to write. could be a string, an int, an array, a bytes/bytearray object, a list etc
        :param endianness: the byte order. default: big
        :return:
        """
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
        """
        set position to 0
        :return:
        """
        self.position = 0
        self.remaining = len(self.data)

    def slice(self):
        """
        slice the buffer at the current position

        note:
            original buffer remain untouched
            position is not incremented
        :return: a ByteBuffer object wrapping data starting from the current position
        """
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

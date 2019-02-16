# PyByteBuffer

A library to manipulate buffers inspired by [Java nio ByteBuffer](https://docs.oracle.com/javase/7/docs/api/java/nio/ByteBuffer.html)

> [>> DOCUMENTATION](https://igio90.github.io/PyByteBuffer/)

## Setup

```
pip3 install PyByteBuffer
```

## Usage

```python
from PyByteBuffer import ByteBuffer

buf = ByteBuffer.allocate(50)
# write byte 0x10 and increment position by 1
buf.put(0x10)
buf.put([0xcc, 0xdd, 0xee])
buf.put('something')
buf.put(bytes([00] * 4))

# endianness
buf.put(123456, 'little')
buf.put(1234561434234234, 'big')

# read 1 byte and increment position by 1
value = buf.get(1)
# read 10 bytes little endian and increment position by 10
value = buf.get(10, 'little')

# other allocations
buf = ByteBuffer.from_hex('deadbeef')
buf = ByteBuffer.wrap(bytes())
```

## About performances
The performance analysis we can do in this library is all around the conversion between int->bytes bytes<-int.

Tested with a cycle of 1/100/500/1000 conversion using python3 builtin api int.to_bytes/from_bytes, struct pack/unpack and a "primitive" solution
posted in [stackoverflow](https://stackoverflow.com/a/35634239)
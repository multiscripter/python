import zlib # Low-level interface to compression and decompression routines compatible with gzip.
# https://docs.python.org/3/library/zlib.html#module-zlib

s = "Low-level interface to compression and decompression routines compatible with gzip."
byteObj = bytes(s, "utf-8")
print(len(byteObj)) # 78

# Классы: zlib, Compress, Decompress.

# zlib.compress(data, level=-1)
# level от -1 по 9
arch = zlib.compress(byteObj, 9)
print(len(arch)) # 54
print(str(zlib.decompress(arch), "utf-8"))
print('zlib.crc32(byteObj):', zlib.crc32(byteObj))

print('zlib.ZLIB_VERSION:', zlib.ZLIB_VERSION)
print('zlib.ZLIB_RUNTIME_VERSION:', zlib.ZLIB_RUNTIME_VERSION)
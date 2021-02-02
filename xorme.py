import sys

for byte in sys.stdin.buffer.read():
  print(chr(byte^1), end='')

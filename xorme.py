import sys

for i in sys.stdin.buffer.read().decode("utf8"):
    #print(chr(ord(i)^1), end='')
    sys.stdout.buffer.write(chr(ord(i)^1).encode("utf8"))
  

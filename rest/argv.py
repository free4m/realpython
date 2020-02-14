import sys
import hashlib


try:
    arg = sys.argv[1]
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} <string to reverse>")
print(arg[::-1])


data = sys.argv[1]
m = hashlib.sha1()
m.update(bytes(data, 'utf-8'))
print(m.hexdigest())

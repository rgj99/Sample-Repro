import math
import sys

from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Rolf"))

r = requests.get("https://hkdir.no")
print(r.status_code)

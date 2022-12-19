"""
Platform module gives information about the
machine where the Python programs executes.
"""

import platform

print(dir(platform))

machine = platform.machine()
operating_system = platform.system()
plt = platform.platform()
info = platform.uname()
node = platform.node()
arq = platform.architecture()

print(machine, operating_system, plt, info, node, arq)
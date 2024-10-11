#! /usr/bin/env python2
import sys

name = "Riaz"
print(name.rjust(20))
print(name.ljust(20, "="))
print(name.rjust(20, "="))
print(name.center(20, "="))
print(sys.argv)
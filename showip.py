#!/usr/bin/python

import sys, time
import RPi.GPIO as IO
from tm1637 import TM1637

IO.setmode(IO.BCM)

Display = TM1637(23, 24, 2)

ip = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]

print ip

for num in ip:
  d = 0
  Display.Clear()
  for n in num:
    Display.Show1(d, int(n))
    d = d + 1
  time.sleep(2)

time.sleep(5)
Display.Clear()

#!/usr/bin/python

import sys, os, time
from time import strftime, gmtime
import RPi.GPIO as IO
from tm1637 import TM1637

IO.setmode(IO.BCM)

Display = TM1637(26, 16, 2)

print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print strftime("%Y-%m-%d %H:%M:%S")

os.environ['TZ'] = 'America/Guayaquil'
time.tzset()

print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print strftime("%Y-%m-%d %H:%M:%S")
hour = strftime("%H")
minute = strftime("%M")

Display.Clear()

if hour < 10:
  Display.Show1(1, hour)
else:
  d = 0
  for n in hour:
    Display.Show1(d, int(n))
    d = d + 1

d = 2
for n in minute:
  Display.Show1(d, int(n))
  d = d + 1

for n in range(0, 10):
  Display.ShowDoublepoint(True)
  time.sleep(1)
  Display.ShowDoublepoint(False)
  time.sleep(1)

Display.Clear()

exit()

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

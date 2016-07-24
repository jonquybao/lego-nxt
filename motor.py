#!/usr/bin/env python

from ev3dev.auto import OUTPUT_A, OUTPUT_D, Motor 
import time
import sys

m_a = Motor(OUTPUT_A)
m_d = Motor(OUTPUT_D)

m_a.speed_sp = 50
m_d.speed_sp = 50

m_a.run_forever()
m_d.run_forever()

print "finished"

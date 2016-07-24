#!/usr/bin/env python

from ev3dev.auto import OUTPUT_A, OUTPUT_D, Motor 
import time
import sys


m_a = Motor(OUTPUT_A)
m_d = Motor(OUTPUT_D)

m_a.stop()
m_d.stop()

print "finished"

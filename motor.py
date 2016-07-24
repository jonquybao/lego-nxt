#!/usr/bin/env python

from ev3dev.auto import OUTPUT_A, OUTPUT_D, Motor 
import time
import sys

m_a = Motor(OUTPUT_A)
m_d = Motor(OUTPUT_D)

m_d.run_forever(duty_cycle_sp = 100)
m_a.run_forever(duty_cycle_sp = 100)
time.sleep(1000)


print "finished"

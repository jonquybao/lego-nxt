#!/usr/bin/env python

from ev3dev.auto import OUTPUT_A, OUTPUT_D, Motor 
import time
import sys


action = sys.argv[1]
m_a = Motor(OUTPUT_A)
m_d = Motor(OUTPUT_D)

if action == 'run':
	m_d.run_forever(duty_cycle_sp = 100)
	m_a.run_forever(duty_cycle_sp = 100)
	time.sleep(1000)
else:
	m_a.stop()
	m_d.stop()

print "finished"

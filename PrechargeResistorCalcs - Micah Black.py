#Capacitor charging from 0 to 95%

import matplotlib.pyplot as plt
import numpy as np

#CAPACITORS
capacitance = 270e-6 #in farads
num_capacitors = 2
total_capacitance = capacitance * num_capacitors

#CHARGE END POINTS
charge_end_percent = 0.95 #1 = 100%
applied_voltage = 150
charge_end_voltage = applied_voltage * charge_end_percent

#RESISTORS
resistance = 300 #in ohms
num_resistors = 1
total_resistance = resistance * num_resistors

time_constant = total_resistance * total_capacitance #not currently used
time_scale = 1e-3 #in seconds
time = 0

current_time = []
current_voltage = []
current_current = []
current_resistor_power = []
total_resistor_energy = []

current_time.append(0)
current_voltage.append(0) #in 
current_current.append(0) #in amps
current_resistor_power.append(0) #in watts
total_resistor_energy.append(0) #in Joules

while current_voltage[-1] < charge_end_voltage:
	#add time stamp to data
	current_time.append(time)
	
	#calculate current using the voltage at the start of the time
	current_current.append((applied_voltage - current_voltage[-1]) / total_resistance)
	
	#calculate voltage rise using V = Q/C = Amps * Seconds / Capacitance
	current_voltage.append(current_voltage[-1] + current_current[-1] * time_scale / total_capacitance)
	
	#calculate power with P = I2R
	current_resistor_power.append(current_current[-1]**2 * total_resistance)
	
	#calculate resistor enery for the last time scale and add it to the previous accumulated energy
	total_resistor_energy.append(total_resistor_energy[-1] + (current_resistor_power[-1] * time_scale))
	
	#update the time
	time += time_scale



#setting up plots
fig, axes = plt.subplots(2)
plt.xlabel('Time (s)')
plt.title('Precharge Resistor and Capacitor Calculations')
ax2 = axes[0].twinx()
ax4 = axes[1].twinx()

#plotting values
axes[0].plot(current_time, current_voltage, 'bo', label = 'Voltage')
ax2.plot(current_time, current_current, 'ro', label = 'Current')
axes[1].plot(current_time, current_resistor_power, 'go', label = 'Resistor Power')
ax4.plot(current_time, total_resistor_energy, 'co', label = 'Resistor Total Energy')

#Setting grid and labels
axes[0].grid(color = 'b')
axes[0].set_ylabel('Voltage', color = 'b')
ax2.grid(color = 'r')
ax2.set_ylabel('Current', color = 'r')
axes[1].grid(color = 'g')
axes[1].set_ylabel('Power', color = 'g')
ax4.grid(color = 'c')
ax4.set_ylabel('Energy', color = 'c')

plt.show()

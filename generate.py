import os
os.environ['KICAD_SYMBOL_DIR'] = "/usr/share/kicad/library"  # Set to the correct directory for your system
os.environ['KISYSMOD'] = "/usr/share/kicad/modules"
from skidl import *

# Use the WS2812 MINI LED symbol from here
lib_search_paths[KICAD].append("kicad-keyboard-parts.pretty/Schematic Library")
footprint_search_paths[KICAD].append('footprints.pretty')

rows = 8
cols = 8

# Standard nets
vcc = Net('VCC')
gnd = Net('GND')

# Create 2d array to hold the leds
leds = [[None] * cols for _ in range(rows)]
positions = []

for row in range(rows):
    for col in range(cols):
        # Create LED parts
        led = Part('kicad-keyboard-parts', 'WS2812B-MINI', footprint='LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm_lowprofile')

        # Hook up power and ground
        led['VDD'] += vcc
        led['VSS'] += gnd

        # Add it to the list of leds
        leds[row][col] = led

        # For convenience, create a list of the positions in order
        positions.append((row, col))

# Create data connections between the leds
for (led1_row, led1_col), (led2_row, led2_col) in [positions[x: x + 2] for x in range(len(positions) - 1)]:
    led1 = leds[led1_row][led1_col]
    led2 = leds[led2_row][led2_col]
    led1['DOUT'] += led2['DIN']

# Create connectors and hook them up to the leds
conn_in = Part('Connector_Generic', 'Conn_01x03', footprint='SMD_Pads:smd_pads_3_in')
conn_in[1] += leds[0][0]['VDD']
conn_in[2] += leds[0][0]['VSS']
conn_in[3] += leds[0][0]['DIN']
conn_out = Part('Connector_Generic', 'Conn_01x03', footprint='SMD_Pads:smd_pads_3_out')
conn_out[1] += leds[-1][-1]['VDD']
conn_out[2] += leds[-1][-1]['VSS']
conn_out[3] += leds[-1][-1]['DOUT']

# Add decoupling caps
n_caps = 9
caps = []
for i in range(n_caps):
    cap = Part('Device', 'C', footprint='Capacitor_SMD:C_0805_2012Metric')
    cap.value = '4.7uf'
    cap[1] += vcc
    cap[2] += gnd
    caps.append(cap)

ERC()

generate_netlist()

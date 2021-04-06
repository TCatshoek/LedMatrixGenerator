import pcbnew
import math

filename = 'matrix/matrix_ws2812bmini.kicad_pcb'
board = pcbnew.LoadBoard('matrix/matrix.kicad_pcb')

layertable = {}
numlayers = 51 # pcbnew.LAYER_ID_COUNT <- doesnt work >_>
for i in range(numlayers):
    layertable[board.GetLayerName(i)] = i
    print("{} {}".format(i, board.GetLayerName(i)))

leds = {module.GetReference(): module for module in board.GetModules() if module.GetReference().startswith('D')}

def calcpos(name):
    num = int(name.replace('D', '')) - 1

    row = math.floor(num / 8)

    if row % 2 == 0:
        x = ((num % 8) * 4) + 2
    else:
        x = (((7 % 8) * 4)) - ((num % 8) * 4) + 2
    y = (math.floor(num / 8) * 4) + 2
    return pcbnew.wxPointMM(x, y)

row = 0
col = 0
for name, led in leds.items():
    led.SetPosition(calcpos(name))

    # Even or uneven rows:
    # if row % 2 == 0:
    if col % 2 == 1:
        led.SetOrientation(90 * 10)
    # else:
    #     if col % 2 == 0:
    #         led.SetOrientation(90 * 10)

    col += 1
    if col >= 8:
        col = 0
        row += 1


pcbnew.SaveBoard(filename, board)
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

generate_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'WS2812B-MINI', 'dest':TEMPLATE, 'tool':SKIDL, 'description':'RGB LED with integrated controller', 'datasheet':'https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf', 'F3':'', 'F0':'D', 'match_pin_substring':False, 'F1':'WS2812B-MINI', 'F2':'LED_SMD:LED_WS2812B-MINI_PLCC4_3.5x3.5mm_P1.75mm', 'keywords':'RGB LED NeoPixel Mini addressable', 'ref_prefix':'D', 'num_units':1, 'fplist':['LED*SK6812MINI*PLCC*3.5x3.5mm*P1.75mm*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm_lowprofile', 'pins':[
            Pin(num='1',name='VDD',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='2',name='DOUT',func=Pin.types.OUTPUT,do_erc=True),
            Pin(num='3',name='VSS',func=Pin.types.PWRIN,do_erc=True),
            Pin(num='4',name='DIN',func=Pin.types.INPUT,do_erc=True)] }),
        Part(**{ 'name':'Conn_01x03', 'dest':TEMPLATE, 'tool':SKIDL, 'description':'Generic connector, single row, 01x03, script generated (kicad-library-utils/schlib/autogen/connector/)', 'datasheet':'~', 'F3':'', 'F0':'J', 'match_pin_substring':False, 'F1':'Conn_01x03', 'F2':'', 'keywords':'connector', 'ref_prefix':'J', 'num_units':1, 'fplist':['Connector*:*_1x??_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'SMD_Pads:smd_pads_3_in', 'pins':[
            Pin(num='1',name='Pin_1',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='Pin_2',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='3',name='Pin_3',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'C', 'dest':TEMPLATE, 'tool':SKIDL, 'description':'Unpolarized capacitor', 'datasheet':'~', 'F3':'', 'F0':'C', 'match_pin_substring':False, 'F1':'C', 'F2':'', 'keywords':'cap capacitor', 'ref_prefix':'C', 'num_units':1, 'fplist':['C_*'], 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':'Capacitor_SMD:C_0805_2012Metric', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,do_erc=True)] })])
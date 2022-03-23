import board
from digitalio import DigitalInOut, Pull, Direction
from adafruit_debouncer import Debouncer

monitor_relay = DigitalInOut(board.GP15)
monitor_relay.direction = Direction.OUTPUT
monitor_relay.value = True #Sets pin high, and NC will have power at relay.

mic_pins = (
    board.GP0, 
    board.GP1, 
    board.GP2, 
    board.GP3, 
)

playout_pins = (
    board.GP4, 
    board.GP5, 
    board.GP6, 
    board.GP7,
)

mic_faders = []   # will hold list of Debouncer objects
for mic_pin in mic_pins:   # set up each pin
    mic_tmp_pin = DigitalInOut(mic_pin) # defaults to input
    mic_tmp_pin.pull = Pull.UP      # turn on internal pull-up resistor
    mic_faders.append( Debouncer(mic_tmp_pin) )

playout_faders = []   # will hold list of Debouncer objects
for playout_pin in playout_pins:   # set up each pin
    playout_tmp_pin = DigitalInOut(playout_pin) # defaults to input
    playout_tmp_pin.pull = Pull.UP      # turn on internal pull-up resistor
    playout_faders.append( Debouncer(playout_tmp_pin) )

mic_opened = [
    "HOST_LIVE ON\r", 
    "GUEST_LIVE ON\r", 
    "\r", 
    "\r", 
    ]


mic_closed = [
    "HOST_LIVE OFF\r", 
    "GUEST_LIVE OFF\r", 
    "\r", 
    "\r", 
    ]

playout_opened = [
    "CARTWALL SHOW\r", 
    "\r", 
    "PLAYER 1-1 START\r", 
    "PLAYER 1-2 START\r",
    ]


playout_closed = [ 
    "CARTWALL HIDE\r", 
    "\r", 
    "PLAYER 1-1 STOP\r", 
    "PLAYER 1-2 STOP\r",
    ]


while True:
    for i in range(len(mic_faders)):
        mic_faders[i].update()
        if mic_faders[i].fell:
            print(mic_opened[i])
            monitor_relay.value = False
        if mic_faders[i].rose:
            print(mic_closed[i])
            monitor_relay.value = True
    
    for i in range(len(playout_faders)):
        playout_faders[i].update()
        if playout_faders[i].fell:
            print(playout_opened[i])
        if playout_faders[i].rose:
            print(playout_closed[i])

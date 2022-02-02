import board
from digitalio import DigitalInOut, Pull
from adafruit_debouncer import Debouncer
pins = (
    board.GP0, 
    board.GP1, 
    board.GP2, 
    board.GP3, 
    board.GP4, 
    board.GP5, 
    board.GP6, 
    board.GP7,
)
faders = []   # will hold list of Debouncer objects

for pin in pins:   # set up each pin
    tmp_pin = DigitalInOut(pin) # defaults to input
    tmp_pin.pull = Pull.UP      # turn on internal pull-up resistor
    faders.append( Debouncer(tmp_pin) )

opened = [
    "Fader 1 open\r", 
    "Fader 2 open\r", 
    "Fader 3 open\r", 
    "Fader 4 open\r", 
    "Fader 5 open\r", 
    "CARTWALL SHOW\r", 
    "PLAYER 1-1 START\r", 
    "PLAYER 1-2 START\r",
    ]


closed = [
    "Fader 1 closed\r", 
    "Fader 2 closed\r", 
    "Fader 3 closed\r", 
    "Fader 4 closed\r", 
    "Fader 5 closed\r", 
    "CARTWALL HIDE\r", 
    "PLAYER 1-1 STOP\r", 
    "PLAYER 1-2 STOP\r",
    ]

print("klar")
while True:
    for i in range(len(faders)):
        faders[i].update()
        if faders[i].fell:
            print(opened[i])
        if faders[i].rose:
            print(closed[i])

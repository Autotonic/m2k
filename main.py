import rtmidi
from pynput.keyboard import Key, Controller

midiin = rtmidi.RtMidiIn()
keyboard = Controller()

table = {
        'C2': 'a',
        'D2': 's',
        'E2': 'd',
        'F2': 'f',
        'G2': 'g',
        'F3': 'h',
        'G3': 'j',
        'A3': 'k',
        'B3': 'l',
        'C4': ';'
        }

def sendkey(midi):
    key = midi.getMidiNoteName(midi.getNoteNumber())
    if key not in table:
        return
    if midi.isNoteOn():
        keyboard.press(table[key])
    elif midi.isNoteOff():
        keyboard.release(table[key])

ports = range(midiin.getPortCount())
if ports:
    print('running')
    midiin.openPort(1)
    while True:
        m = midiin.getMessage(0)
        if m:
            sendkey(m)
else:
    print('NO MIDI INPUT PORTS!')

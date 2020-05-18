import json
from pathlib import Path
from typing import NoReturn
from rtmidi import RtMidiIn
from pynput.keyboard import Controller


class M2K:
    def __init__(self):
        self.config_path = Path().cwd() / "m2k.json"
        self.table: dict = {}
        self.midi = RtMidiIn()
        self.keyboard = Controller()

    def set_config(self) -> NoReturn:
        with open(str(self.config_path), "r") as j:
            self.table = json.load(j)

    def update_config(self, update: dict) -> NoReturn:
        with open(str(self.config_path), "w") as new:
            new.write(json.dumps(update))
        self.set_config()

    def send_key(self, midi_message) -> NoReturn:
        key = midi_message.getMidiNoteName(midi_message.getNoteNumber())
        if key not in self.table:
            return
        if midi_message.isNoteOn():
            self.keyboard.press(self.table[key])
        elif midi_message.isNoteOff():
            self.keyboard.release(self.table[key])

    def run(self) -> NoReturn:
        ports = range(self.midi.getPortCount())
        if ports:
            print("Running")
            self.midi.openPort(0)
            while True:
                if midi_message := self.midi.getMessage(0):
                    self.send_key(midi_message)


if __name__ == "__main__":
    m2k = M2K()
    if m2k.config_path.exists():
        m2k.set_config()
        m2k.run()

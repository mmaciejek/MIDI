import mido
import tkinter as tk
from tkinter import Scale

# Replace 'Sterownik IAC Magistrala 1' with the actual name of your MIDI output port (video synthesis program)
output_port_name = 'Sterownik IAC Magistrala 1'

# Function to send a MIDI CC message
def send_cc_message(channel, control, value):
    cc_number = 20 + (channel * 32) + control
    midi_message = mido.Message('control_change', channel=channel, control=cc_number, value=value)
    outport.send(midi_message)

class MidiControllerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MIDI Controller App")

        # Create and pack a fader for each control
        self.create_fader(channel=1, control=20, label="ch1 hue")
        self.create_fader(channel=1, control=21, label="ch1 saturation")
        self.create_fader(channel=1, control=22, label="ch1 brightness")

        self.create_fader(channel=1, control=-25, label="blur")
        self.create_fader(channel=1, control=24, label="sharpen")

        self.create_fader(channel=1, control=28, label="fb0 key V")
        self.create_fader(channel=1, control=29, label="fb0 mix")
        self.create_fader(channel=1, control=30, label="fb0 delay")
        self.create_fader(channel=1, control=4, label="fb0 x")
        self.create_fader(channel=1, control=3, label="fb0 y")
        self.create_fader(channel=1, control=12, label="fb0 z")
        self.create_fader(channel=1, control=11, label="fb0 rotate")
        self.create_fader(channel=1, control=5, label="fb0 hue")
        self.create_fader(channel=1, control=2, label="fb0 sat")
        self.create_fader(channel=1, control=13, label="fb0 bright")
        self.create_fader(channel=1, control=16, label="fb0 huemod")
        self.create_fader(channel=1, control=10, label="fb0 hueoffset")
        self.create_fader(channel=1, control=17, label="fb0 huelfo")

        self.create_fader(channel=1, control=31, label="fb1 key V")
        self.create_fader(channel=1, control=27, label="fb1 mix")
        self.create_fader(channel=1, control=26, label="fb1 delay")
        self.create_fader(channel=1, control=6, label="fb1 x")
        self.create_fader(channel=1, control=1, label="fb1 y")
        self.create_fader(channel=1, control=14, label="fb1 z")
        self.create_fader(channel=1, control=9, label="fb1 rotate")
        self.create_fader(channel=1, control=7, label="fb1 hue")
        self.create_fader(channel=1, control=0, label="fb1 sat")
        self.create_fader(channel=1, control=15, label="fb1 bright")
        self.create_fader(channel=1, control=18, label="fb1 huemod")
        self.create_fader(channel=1, control=8, label="fb1 hueoffset")
        self.create_fader(channel=1, control=19, label="fb1 huelfo")

    def create_fader(self, channel, control, label):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP, padx=10, pady=5)

        label_widget = tk.Label(frame, text=label)
        label_widget.pack(side=tk.LEFT)

        fader = Scale(frame, from_=0, to=127, orient=tk.HORIZONTAL, length=200, command=lambda value, ch=channel, ctrl=control: send_cc_message(ch, ctrl, int(value)))
        fader.set(0)
        fader.pack(side=tk.LEFT)

if __name__ == "__main__":
    # Check available output ports
    print("Output Ports:", mido.get_output_names())

    # Select the specified output port
    outport = mido.open_output(output_port_name)

    # Create the Tkinter root window and start the GUI application
    root = tk.Tk()
    app = MidiControllerApp(root)
    root.mainloop()

    # Close the output port when the GUI is closed
    outport.close()

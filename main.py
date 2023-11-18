import mido
import time

# Replace 'Your_Output_Port' with the actual name of your MIDI output port
output_port_name = 'Sterownik IAC Magistrala 1'

# Check available input and output portsa
print("Input Ports:", mido.get_input_names())
print("Output Ports:", mido.get_output_names())

# Select the specified output port
outport = mido.open_output(output_port_name)

try:
    while True:
        # Create a MIDI note_on message and send it
        note_on = mido.Message('note_on', note=60, velocity=64)
        outport.send(note_on)

        # Wait for a short duration
        time.sleep(1)

        # Create a MIDI note_off message and send it
        note_off = mido.Message('note_off', note=60, velocity=64)
        outport.send(note_off)

        # Wait before triggering the next note
        time.sleep(1)

except KeyboardInterrupt:
    # Close the output port if the script is interrupted
    outport.close()
    print("\nScript terminated by user.")

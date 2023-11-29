import mido

# Get a list of available MIDI input ports
input_ports = mido.get_input_names()

# Print the list of input ports
print("Available MIDI Input Ports:")
for port in input_ports:
    print(port)

# Choose the MIDI input port you want to use
selected_input_port = 'MSI 0'

# Open the selected input port
input_port = mido.open_input(selected_input_port)

# Print incoming MIDI messages
print("Listening for MIDI messages. Press Ctrl+C to exit.")
try:
    for message in input_port:
        print("Received:", message)
except KeyboardInterrupt:
    # Handle Ctrl+C to exit gracefully
    pass
finally:
    # Close the input port when done
    input_port.close()

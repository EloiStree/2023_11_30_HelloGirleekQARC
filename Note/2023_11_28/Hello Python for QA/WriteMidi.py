import mido
import time

def press_and_release_all_notes(port):
    # Iterate through all MIDI notes (0 to 127)
    for note in range(128):
        # Send a Note On message (velocity 64, you can adjust it if needed)
        message = mido.Message('note_on', note=note, velocity=64)
        port.send(message)
        
        # Sleep for a short duration (you can adjust it based on your needs)
        time.sleep(0.1)
        
        # Send a Note Off message
        message = mido.Message('note_off', note=note, velocity=64)
        port.send(message)

if __name__ == "__main__":
    # List available MIDI ports
    print("Available MIDI Ports:")
    for port in mido.get_output_names():
        print(port)

    # Ask the user to select a MIDI port
    selected_port = input("MSI 1")

    # Open the selected MIDI port
    try:
        with mido.open_output(selected_port) as port:
            while True:
                print(f"Pressing and releasing all notes on {selected_port}...")
                press_and_release_all_notes(port)
    except Exception as e:
        print(f"Error: {e}")

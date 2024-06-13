# Python Keylogger

This Python script captures keystrokes from the keyboard and logs them into a file. It utilizes the `pynput` library to monitor keyboard input.

## Features

- Captures keystrokes and records them into a specified text file.
- Handles special keys like space, enter, tab, backspace, and escape for more readable logging.
- The logging functionality runs in the background until manually stopped.

## Dependencies

- [pynput](https://pypi.org/project/pynput/): A Python library for monitoring and controlling input devices.

## Usage

1. Install the required dependencies using pip:

    ```bash
    pip install pynput
    ```

2. Run the script:

    ```bash
    python keylogger.py
    ```

3. The script will start logging keystrokes into the `keylog.txt` file in the same directory where the script is located.

4. Press `Esc` key to stop the keylogger.

## Customization

- **Log File**: You can change the log file path by modifying the `log_file` variable in the script.

## Disclaimer

This script is for educational purposes only. Ensure that you have appropriate permissions before running it on any device.

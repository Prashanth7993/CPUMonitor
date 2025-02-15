import time
from process_utils import handle_process

def monitor_cpu():
    """ Continuously monitor CPU usage every 5 seconds. """
    while True:
        handle_process()
        time.sleep(5)

if __name__ == "__main__":
    monitor_cpu()

"""
main runner for automat
"""
from src.manager import Manager

def run_automat():
    """
    run automat:
    - listen for RFID tag signal
    - when a signal comes in, ask the manager to handle it
    """
    manager = Manager()
    while True:
        setting = raw_input('Setting:')
        manager.check_setting(setting)

if __name__=="__main__":
    run_automat()

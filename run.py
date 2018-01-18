"""
main runner for automat
"""
import sys
from src.manager import Manager

def run_automat(config_file):
    """
    run automat:
    - listen for RFID tag signal
    - when a signal comes in, ask the manager to handle it
    """
    manager = Manager(config=config_file)
    while True:
        setting = raw_input('Setting:')
        manager.check_setting(setting)

if __name__=="__main__":
    try:
        config_file = sys.argv[1]
    except IndexError:
        config_file = './config'
        print "Warning: no config file specified, using ./config"
    run_automat(config_file)

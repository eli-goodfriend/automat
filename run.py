"""
main runner for automat
"""
import sys
from src.manager import Manager
from src.read_setting import Reader

def run_automat(config_file):
    """
    run automat:
    - listen for RFID tag signal
    - when a signal comes in, ask the manager to handle it
    """
    manager = Manager(config=config_file)
    reader = Reader(config=config_file)
    while True:
        setting = reader.get_input()
        manager.check_setting(setting)

if __name__=="__main__":
    try:
        config_file = sys.argv[1]
    except IndexError:
        config_file = './config'
        print "Warning: no config file specified, using ./config"
    run_automat(config_file)

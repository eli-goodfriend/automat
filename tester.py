"""
run tests in the test dir
"""
from test.tests import TestSound

def run_tester():
    """
    run tests in the test dir
    """
    tester = TestSound()
    tester.run()

if __name__=="__main__":
    run_tester()

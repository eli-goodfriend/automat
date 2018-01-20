"""
run tests in the test dir
"""
from test.tests import TestSound, TestPandora

def run_tester():
    """
    run tests in the test dir
    """
    #tester = TestSound()
    #tester.run()

    tester = TestPandora()
    tester.run()

if __name__=="__main__":
    run_tester()

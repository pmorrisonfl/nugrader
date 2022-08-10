import check50
import os
STUDENT = os.getenv('STUDENT')

@check50.check()
def exists():
    """check for whether myNetID.txt exists"""
    check50.exists("myNetID.txt")

@check50.check(exists)
def file_contains_netid():
    """Check whether myNetID.txt contains student netid"""
    expected = STUDENT
    check50.run("cat myNetID.txt").stdout(STUDENT, regex=False)

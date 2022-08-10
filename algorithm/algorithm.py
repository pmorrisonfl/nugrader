import check50
import os

@check50.check()
def exists():
    """check for whether answer file exists"""
    check50.exists("answer.txt")

@check50.check(exists)
def file_contains_netid():
    """Check whether answer.txt contains correct string"""
    check50.run("cat answer.txt").stdout("-36 -35 -32 -27 -20 -11 0 13 28 45 64 85 108 133 160 189 220 253", regex=False)

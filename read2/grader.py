import check50
import os

@check50.check()
def exists():
    """check for whether answer file exists"""
    check50.exists("answer.txt")

@check50.check(exists)
def file_contains_netid():
    """Check whether answer.txt contains correct string"""
    check50.run("cat answer.txt").stdout("a = 6, b = 43, c = 1\na = 17, b = 43, c = 23\na = 17, b = 1, c = 23\n", regex=False)

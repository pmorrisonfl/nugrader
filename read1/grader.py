import check50
import os

@check50.check()
def exists():
    """check for whether answer file exists"""
    check50.exists("answer.txt")

@check50.check(exists)
def file_contains_netid():
    """Check whether answer.txt contains correct string"""
    check50.run("cat answer.txt").stdout("a is {0, 3, 6, 30, 24}\n*p is 6\n", regex=False)

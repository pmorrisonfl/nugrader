import check50
import os

@check50.check()
def exists():
    """check for whether answer file exists"""
    check50.exists("answer.txt")

@check50.check(exists)
def file_contains_netid():
    """Check whether answer.txt contains correct string"""
    check50.run("cat answer.txt").stdout("a is 3\nb is 8\na * i + b = 8\na * i + b = 12\na * i + b = 16\na * i + b = 20\na is 5\nb is 6\n", regex=False)

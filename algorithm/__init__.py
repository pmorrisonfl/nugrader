import check50

@check50.check()
def algorithm18N6():
    """algorithm18N6"""
    check50.run("cat answer.txt").stdout("-36 -35 -32 -27 -20 -11 0 13 28 45 64 85 108 133 160 189 220 253", regex=False).exit(0)
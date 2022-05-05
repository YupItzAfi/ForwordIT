class Some:
    somenum = 0

    def __init__(self, somenum=None) -> None:
        self.somenum = somenum

    def sayNum(self, somenum=somenum):
        print(Some.somenum)

    def printSomenum(self):
        return self


d = Some(101)
d.sayNum("Something")

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr=[]
        self.prr=[]
        self.mini=100000000000
    def push(self, x: int) -> None:
        self.arr.append(x)
        if(x<self.mini):
            self.mini=x
        self.prr.append(self.mini)
    def pop(self) -> None:
        self.arr=self.arr[:-1]
        self.prr=self.prr[:-1]
        if(len(self.prr)>0):
            self.mini=self.prr[-1]
        else:
            self.mini=100000000000

    def top(self) -> int:
        return(self.arr[-1])

    def getMin(self) -> int:
        return(self.prr[-1])
class DoubleStackQueue:

    def __init__(self):
        self.stac = []
        self.stac2 =[]

    def push(self, x: int) -> None:
        self.stac.append(x)

    def pop(self) -> int:
        while len(self.stac) != 1:
            self. stac2.append(self.stac.pop())
        ans = self.stac[0]
        self. stac.pop()
        while len(self.stac2) != 0:
            self.stac.append(self.stac2.pop())
        return ans
    def peek(self) -> int:
        return self.stac[0]
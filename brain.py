class Queen:
    def __init__(self, n):
        self.n = n
        self.solution = [None] * n
        self.row = [0] * n
        self.ldiag = [0] * (2 * n - 1)
        self.rdiag = [0] * (2 * n - 1)
        self.nfound = 0
        self.result = []

    def solve(self, x=0):
        for y in range(self.n):
            if self.safe(x, y):
                self.update(x, y)
                if x + 1 == self.n:
                    self.display()
                else:
                    self.solve(x + 1)
                self.remove(x, y)

    def safe(self, x, y):
        return not self.row[y] and not self.ldiag[x - y] and not self.rdiag[x + y]

    def update(self, x, y):
        self.row[y] = 1
        self.ldiag[x - y] = 1
        self.rdiag[x + y] = 1
        self.solution[x] = y

    def remove(self, x, y):
        self.solution[x] = None
        self.row[y] = 0
        self.ldiag[x - y] = 0
        self.rdiag[x + y] = 0

    def display(self):
        self.nfound += 1
        self.result.append([i for i in self.solution])


def main(n):
    q = Queen(n)
    q.solve()
    position_set = q.result
    return position_set



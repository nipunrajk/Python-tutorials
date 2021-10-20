Q) Define iteror for printing square number, where we define method __iter()__ and __next__() which are two method called during python iteration. 

class Square:
    def __init__(self, i=0, j=1):
        self.i = i
        self.j = j

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.j:
            s = self.i ** 2
            self.i += 1
            return s
        else:
            raise StopIteration


for x in Square(1,4):
    print(x)


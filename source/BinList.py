
class BinList(list):

    def __init__(self, size):
        super().__init__([0])
        self.bin_size = size
        self.bin_access = 0

    def __getitem__(self, key):
        self.bin_access += 1
        return super().__getitem__(key)


    def fit(self, index, object):
        return self.__getitem__(index) + object <= self.bin_size


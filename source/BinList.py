class BinList(list):

    def __init__(self, size):
        super().__init__([0])
        self.bin_size = size
        self.bin_access = 0

    def __getitem__(self, key):
        self.bin_access += 1
        return super().__getitem__(key)

    def __iter__(self):
        self.m_iter = super().__iter__()
        return self

    def __next__(self):
        try:
            m_next = self.m_iter.__next__()
            self.bin_access += 1
            return m_next
        except StopIteration: # 'cause we don't wanna count past the end
            raise StopIteration

    def fit(self, index, object):
        return self.__getitem__(index) + object <= self.bin_size


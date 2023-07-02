class Iterator(object):
    iterator: int
    incrementor: int
    DEFAULT_INCREMENTOR: int = 1
    DEFAULT_ITERATOR_START: int = 0
    DEFAULT_ITERATOR_END: int = None

    def __init__(self):
        self.iterator = 0
        self.incrementor = self.DEFAULT_INCREMENTOR

    ##########################################################
    #
    ##########################################################
    def next(self):
        if self.iterator >= self.DEFAULT_ITERATOR_END:
            self.iterator = self.iterator + self.incrementor

    ##########################################################
    #
    ##########################################################
    def clear_iterator(self):
        self.iterator = self.DEFAULT_ITERATOR_START

    ##########################################################
    #
    ##########################################################
    def set_incrementor(self, new_incrementor: int):
        self.incrementor = new_incrementor

    ##########################################################
    #
    ##########################################################
    def reset_incrementor(self):
        self.incrementor = self.DEFAULT_INCREMENTOR

class RingBuffer:
    def __init__(self, capacity):
        #capacity of the buffer
        self.capacity = capacity
        #index of oldest value in buffer
        self.oldest = None
        #where buffer values are stored
        self.buffer = []

    def append(self, item):
        #if capacity has been reached replace the item at the
        #oldest index with the new item and adjust the oldest
        #by one index or reset to zero if iterating it again
        #will go past capcity.
        if len(self.buffer) == self.capacity:
            self.buffer[self.oldest] = item
            if self.oldest < self.capacity - 1:
                self.oldest += 1
            else:
                self.oldest = 0
        else:
            if not self.oldest:
                self.oldest = 0
            self.buffer.append(item)

    def get(self):
        #return buffer
        return self.buffer


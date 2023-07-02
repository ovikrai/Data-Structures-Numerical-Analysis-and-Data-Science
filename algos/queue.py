###############################################
# Structure: Queue
# LIFO: Last In, First Out
# Complexity:
#   Read:
#   Write:
###############################################
class Queue(object):
    def __init__(self, elements=list()):
        self.elements = elements

    def length(self):
        return len(self.elements) - 1

    def is_empty(self):
        if self.length() == 0:
            return True
        else:
            return False

    # Add
    def enqueue(self, element):
        self.elements.append(element)

    # Remove
    def dequeue(self):
        self.elements.pop(0)
###############################################

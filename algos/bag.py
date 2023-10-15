###############################################
# Structure: Bag, abstraction of the mathematical set
# Complexity:
#   Read:
#   Write:
###############################################
class Bag(object):
    elements: set

    def __init__(self):
        self.elements = set()

    def get_item(self, target_element):
        for element in self.elements:
            if target_element == element:
                return element
            else:
                return -1

    def size(self) -> int:
        return len(self.elements) - 1

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def add(self, element):
        self.elements.add(element)

    def remove(self, element):
        self.elements.remove(element)

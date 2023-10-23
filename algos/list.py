from typing import Any, NoReturn


###############################################
# Structure: List: An mutable set of elements with order
# Complexity:
#   Read:
#   Write:
###############################################
class List(object):
    elements: list

    def __init__(self, size: int):
        self.elements = []

    def size(self):
        return len(self.elements)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def count_elements(self, element: Any) -> int:
        return self.elements.count(element)

    def get_element(self, index) -> Any:
        return self.elements[index]

    def get_object_original(self) -> list:
        return self.elements

    def get_object_copy(self) -> list:
        return self.elements.copy()

    def remove_all_elements(self) -> NoReturn:
        self.elements.clear()

    def remove_one_element(self, index) -> NoReturn:
        self.elements.pop(index)

    def add_one_element(self, element) -> NoReturn:
        self.elements.append(element)

    def add_many_elements(self, *elements) -> NoReturn:
        self.elements.extend(elements)

    def set_one_element(self, index, element: Any) -> NoReturn:
        self.elements.insert(index, element)

    def render(self) -> NoReturn:
        print('########## START: LIST RENDERING REPRESENTATION #########')
        print('########## | LIST: SIZE', self.size())
        print('########## |', self.elements)
        print('########## END: LIST RENDERING REPRESENTATION ######### \n')

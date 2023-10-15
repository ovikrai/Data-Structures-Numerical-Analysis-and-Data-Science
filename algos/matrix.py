from typing import List


class Matrix:
    matrix: List[List[float]]

    # Matrix initialization
    def __int__(self, n: int, s_type='float'):
        for i in range(0, n + 1, 1):
            # Initialize with function provided values
            self.matrix.append([])
            for j in range(0, n + 1, 1):
                # Matrix initialization with Zeros
                self.matrix[i].append(0.0)

    def update_element(self, value, i, j):
        self.matrix[i][j] = value

    def get_element(self, i, j):
        return self.matrix[i][j]

    def get_object_original(self):
        return self.matrix

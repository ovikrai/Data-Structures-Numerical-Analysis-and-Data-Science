import numpy as np
import tensorflow as tf
from algos.model import Model


class FeedForward(Model):

    def __init__(self,
                 x_train: np.ndarray,
                 x_test: np.ndarray,
                 y_train: np.ndarray,
                 y_test: np.ndarray,
                 ):
        super().__init__(x_train, x_test, y_train, y_test)

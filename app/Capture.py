import ctypes
import cv2
from cv2 import VideoCapture
from typing import Union


class Capture:
    def __init__(self, uri: str):
        self.uri = uri
        self.connection = self.connect()

    def __del__(self):
        self.connection.release()
        cv2.destroyAllWindows()

    def connect(self) -> VideoCapture:
        capture = cv2.VideoCapture(self.uri)
        capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        return capture

    def getImage(self) -> Union[ctypes.Array, bool]:
        ret, image = self.connection.read()
        if ret:
            return image
        else:
            return False

    def showImage(self, image: ctypes.Array) -> None:
        cv2.imshow('IP Camera', image)
        cv2.waitKey(1)

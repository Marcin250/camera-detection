import cv2
from cv2 import VideoCapture
from typing import Union
from numpy import ndarray


class Capture:
    def __init__(self, uri: str):
        self.__uri = uri
        self.__connection = self.__connect()

    def __del__(self):
        self.__connection.release()
        cv2.destroyAllWindows()

    def getConnection(self) -> VideoCapture:
        return self.__connection

    def reConnect(self) -> VideoCapture:
        self.__connection = self.__connect()

        return self.__connection

    def getImage(self) -> Union[ndarray, bool]:
        ret, image = self.__connection.read()

        if ret:
            return image
        else:
            return False

    def showImage(self, image) -> int:
        cv2.imshow('IP Camera', image)

        return cv2.waitKey(1)

    def __connect(self) -> VideoCapture:
        capture = cv2.VideoCapture(self.__uri)
        capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        return capture

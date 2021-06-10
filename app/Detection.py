import cv2
import os
from imageai.Detection import VideoObjectDetection as Detection
import Capture
from matplotlib import pyplot as plt


class ObjectDetection:
    def __init__(self):
        self.__detection = self.__loadDetection()

    def detect(self, capture: Capture):
        rootDirectory = os.path.normpath(os.getcwd() + os.sep + os.pardir)
        self.__detection.detectObjectsFromVideo(
            camera_input=capture,
            output_file_path=rootDirectory + '/resources/yikes.avi',
            # save_detected_video=False,
            frames_per_second=10,
            minimum_percentage_probability=30,
            # return_detected_frame=True
        )

    def displayFrame(self, frameNumber, outputArray, outputCount, frame):
        plt.title("IPCamera")
        plt.imshow(frame, interpolation="none")
        plt.pause(0.01)

    def __loadDetection(self) -> Detection:
        rootDirectory = os.path.normpath(os.getcwd() + os.sep + os.pardir)
        detection = Detection()
        detection.setModelTypeAsYOLOv3()
        detection.setModelPath(rootDirectory + '/resources/yolo.h5')
        detection.loadModel()

        return detection


class MotionDetection:
    def detect(self, frame, nextFrame):
        difference = cv2.absdiff(frame, nextFrame)
        gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresholdRet, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(threshold, None, iterations=3)
        contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 2200:
                continue

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame

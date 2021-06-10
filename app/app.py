import cv2

import Capture
import Detection
import os
from dotenv import load_dotenv


def shouldStop(pressedKeyValue: int) -> bool:
    return pressedKeyValue == 27

def sourceCapture(capture: Capture):
    stop = False
    while not stop:
        if capture.getConnection().isOpened():
            image = capture.getImage()
            if not isinstance(image, bool):
                stop = shouldStop(capture.showImage(image))
            else:
                print('Failed to get image')
        else:
            print('Failed to connect Camera')

def motionDetection(capture: Capture):
    detection = Detection.MotionDetection()
    frame = capture.getImage()

    if isinstance(frame, bool):
        print('Failed to get image')
        return

    stop = False
    while not stop:
        if capture.getConnection().isOpened():
            nextFrame = capture.getImage()
            if not isinstance(nextFrame, bool):
                stop = shouldStop(capture.showImage(detection.detect(frame, nextFrame)))
                frame = nextFrame
            else:
                print('Failed to get image')
        else:
            print('Failed to connect Camera')

def objectDetection(capture: Capture):
    detection = Detection.ObjectDetection()
    detection.detect(capture)

    # stop = False
    # while not stop:
    #     if capture.getConnection().isOpened():
    #         frame = capture.getImage()
    #         if not isinstance(frame, bool):
    #             stop = shouldStop(capture.showImage(detection.detect(frame)))
    #         else:
    #             print('Failed to get image')
    #     else:
    #         print('Failed to connect Camera')


load_dotenv()
capture = Capture.Capture(os.environ.get('CAMERA_STREAM_URI'))
objectDetection(capture)

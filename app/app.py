import Capture
import os
from dotenv import load_dotenv

load_dotenv()

capture = Capture.Capture(os.environ.get('CAMERA_STREAM_URI'))

while True:
    if capture.connection.isOpened():
        image = capture.getImage()
        if ~isinstance(image, bool):
            capture.showImage(image)

import Capture
import os
from dotenv import load_dotenv

load_dotenv()

capture = Capture.Capture(os.environ.get('CAMERA_STREAM_URI'))

while True:
    if capture.getConnection().isOpened():
        image = capture.getImage()
        if ~isinstance(image, bool):
            capture.showImage(image)
        else:
            print('Failed to get image')
    else:
        print('Failed to connect Camera')

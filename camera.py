import cv2 as cv

"""
The Camera class encapsulates the functionality for accessing and capturing video frames
from a camera using OpenCV. It provides methods to initialize the camera, retrieve frames, 
and release the camera resources.
"""
class Camera:
    """
         Initializes the Camera object by attempting to open the default camera (usually the
         webcam) and setting the width and height properties based on the camera's capabilities.
         """
    def __init__(self):
        # Open the default camera (camera index 0).
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Cannot open camera.")
        # Retrieve the width and height of the frames captured by the camera.
        # These properties are used to understand the resolution of the captured frames.
        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    # Captures a single frame from the camera. Converts the frame from BGR to RGB format
    # which is commonly used in image processing tasks.
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None
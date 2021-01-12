from time import time
import cv2

class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def release(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()

        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV

        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()
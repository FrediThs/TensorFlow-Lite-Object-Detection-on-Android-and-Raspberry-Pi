# Define VideoStream class to handle streaming of video from webcam in separate process thread
# Source: Adrian Rosebrock, PyImageSearch
import argparse
import cv2
from threading import Thread

class VideoStream:
    """ Camera object that controls video streaming from"""
    def __init__(self, resolution=(640,480),framerate=90):
        # initiliaze the PiCamera and the camera image stream
        self.stream = cv2.VideoCapture(0)
        ret = self.stream.set(cv2,CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
        ret = self.stream.set(3,resolution[0])
        ret = self.stream.set(4,resolution[1])

        # Read first frame from the stream
        (self.grabbed, self.frame) = self.stream.read()
    
        # Variable to control when the camera is stopped
        self.stopped = False

    def start(self):
        # start the thread that reads frames from the video
        Thread(target=self.upgdate,args=()).start()
        return self

# class for temporary images and deletion
import uuid
import os

class TempImage:
    def __init__(self, basePath="./",ext=".jpg"):
        #construct file path
        self.path="{base_path}/{rand}{ext}".format(
            base_path=basePath, rand=str(uuid.uuid4()),ext=ext)
    
    def cleanup(self):
        # remove the file
        os.remove(self.path)
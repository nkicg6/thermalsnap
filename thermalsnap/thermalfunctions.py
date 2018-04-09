# holds thermal functions class
# note, a lot of big dependencies here, I think opencv and numpy cant be avoided,
# but I will try to remove matplotlib and scipy
# right now python2 due to opencv available on apt-get
import os
import datetime
import subprocess
import time
import json
import email

try:
    #import picamera
    from Lepton import Lepton
    import numpy as np
    import cv2
    import matplotlib.pyplot as plt
    from scipy import misc
except ImportError as e:
    print("a package could not be imported. please pip install or\
    sudo apt-get install {}".format(e))


class ThermalFunctions:
    def __init__(self, parent, controller):
        self.controller = controller
        self.path_to_preview_binary = ["/home/pi/LeptonModule/software/raspberrypi_video/raspberrypi_video"]
        self.thermal_preview_subprocess = None
        self.debug_status = True
        #self.camera = picamera.PiCamera()
        #self.camera.resolution = (640, 480)
        #self.camera.framerate = 24
        if os.uname()[4] != "armv7l":
            print("Pi not detected, debug mode only")
            print("system {} detected.".format(os.uname()[4]))
            self.debug_status = True
        else:
            print("{} system detected, continuing".format(os.uname()[4]))
            self.debug_status = False

    def start_thermal(self):
        print("thermal subprocess")
        try:
            self.thermal_preview_subprocess = subprocess.Popen(self.path_to_preview_binary)
            #self.camera.start_preview(fullscreen=False,
            #                          window=(100,100,500,500))
        except:
            print("coult not start preview")

    def stop_thermal(self):
        try:
            print("stop thermal subprocess")
            self.thermal_preview_subprocess.kill()
            #self.camera.stop_preview()
        except:
            print("no process to kill")

    def take_picture(self):
        self.stop_thermal()
        # print(self.controller.shared_data["picture_user_name"].get())
        # print(self.controller.shared_data["picture_user_email"].get())
        print(" if thermal subprocess, stop")
        try:
            self.make_image_name()
            with Lepton() as l:
                print("made it here")
                a, _ = l.capture()
                cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)
                np.right_shift(a, 8, a)
                cv2.imwrite(self.controller.shared_data["current_image_name"],a)
                a = misc.imread(self.controller.shared_data["current_image_name"])
                bigger = misc.imresize(a, (480,640), interp="bilinear")
                cmap = plt.cm.hot
                plt.imsave(self.controller.shared_data["current_image_name"],bigger, cmap=cmap)
                print("picture saved as {}".format(self.controller.shared_data["current_image_name"]))
        except Exception as e:
            print("no picture taken, error {}".format(e))

    def make_image_name(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
        home_dir = self.controller.shared_data["home_dir"]
        self.controller.shared_data["current_image_name"] = home_dir+ "/"+ self.controller.shared_data["picture_user_name"].get().replace(" ", "_") + "_" + timestamp+".png"
        print(self.controller.shared_data["current_image_name"])


    def email_picture(self):
        print("email thermal")
        self.controller.shared_data["current_image_name"] = None
        print("reset current image name to {}".format(self.controller.shared_data["current_image_name"]))

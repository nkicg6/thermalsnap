# holds thermal functions class
import os
import subprocess
try:
    import picamera
except ImportError:
    print("picamera could not be imported.")


class ThermalFunctions:
    def __init__(self, parent, controller):
        self.controller = controller
        self.path_to_preview_binary = ["/home/pi/LeptonModule/software/raspberrypi_video/raspberrypi_video"]
        self.path_to_picture_binary = [""]
        self.thermal_preview_subprocess = None
        self.debug_status = True

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
        except:
            print("coult not start preview")

    def stop_thermal(self):
        try:
            print("stop thermal subprocess")
            self.thermal_preview_subprocess.kill()
        except:
            print("no process to kill")


    def take_picture(self):
        self.stop_thermal(self)
        print(" if thermal subprocess, stop")
        try:

        print("then new subprocess to take picture")

    def email_picture(self):
        print("email thermal")

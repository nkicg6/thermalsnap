# holds thermal functions class
import os
import subprocess

class ThermalFunctions:
    def __init__(self, parent, controller):
        self.controller = controller
        if os.uname()[4] != "Linux":
            print("Pi not detected, debug mode only")
        else:
            pass

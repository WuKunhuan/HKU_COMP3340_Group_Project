
import os, sys, subprocess

class setup:
    
    def __init__(self): 
        os.system("clear")
        if (os.name == 'nt'):
            raise Exception (f"[Error] Please use Linux or Mac, but not Windows to work with this notebook")

        self.path = str(subprocess.check_output("pwd"))
        self.path = self.path[2:len(self.path)-3:1]
        print(f"Path: {self.path}")

        # Import Pytorch
        try:
            import torch
            import torch.nn as nn
        except ImportError:
            os.system("clear")
            raise Exception(f"[Error] import pytorch failed. Run \"conda install pytorch\" in a terminal under {path}, then run the setup again. ")
        print ("[Package] import pytorch succeeded. ")

        # Import numpy
        try:
            import numpy as np
        except ImportError:
            os.system("clear")
            raise Exception(f"[Error] import numpy failed. Run \"conda install numpy\" in a terminal under {path}, then run the setup again. ")
        print ("[Package] import numpy succeeded. ")

        # Import torchvision
        try:
            import torchvision
            from torchvision import transforms
        except FileNotFoundError:
            os.system("clear")
            raise Exception(f"[Error] import torchvision failed. Run \"conda install torchvision\" in a terminal under {path}, then run the setup again. ")
        print ("[Package] import torchvision succeeded. ")
        print ("")
        print ("COMP3340_GP setup finished. ")
        
        


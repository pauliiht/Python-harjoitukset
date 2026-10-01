## jos ehto täyttyy, eli asiakkaalla on vähintään 5€ rahaa,
# niin ohjelma suorittaa ehdollisen lohkon (sisennetty komento)

import math


raha = float(input("Kuinka paljon sinulla on rahaa? "))
             
if raha >= 5:
    print("Voit ostaa kahvin!")
                 
print("Hyvää päivänjatkoa!")
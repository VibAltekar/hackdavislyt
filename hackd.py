import sys
sys.path.insert(0,"/Users/vibhav/Downloads/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib")
import time
import os
import Leap, sys, thread, time
import serial

ser = serial.Serial(port='/dev/tty.usbmodem1411',baudrate=9600)
class execute(Leap.Listener):

    def on_frame(self, controller):
        frame = controller.frame()
        for hand in frame.hands:
            handType = "Left hand" if hand.is_left else "Right hand"
            if handType[0] == "L":
                #print("1")
                #os.system("particle serial flash left.ino")
                ser.write("1")
                print("Left")
                time.sleep(.5)
                ser.write("2")

            if handType[0] == "R":
                #os.system("particle serial flash right.ino")
                #print("0")
                ser.write("0")
                print("Right")
                time.sleep(.5)
                ser.write("2")

            

def main():

    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)

   

if __name__ == "__main__":
    main()

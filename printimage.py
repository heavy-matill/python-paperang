#!/usr/bin/env python3
import config
import time
import hardware
import image_data
import sys

if len(sys.argv)<2:
    print('No images passed to print. Append the filepaths to the script call e.g. python3 printimage.py img1.jpg img2.jpg')
class Paperangg_Printer:
    def __init__(self):
        if hasattr(config, "macaddress"):
            print("attempting test print to MAC address \"% s\""% config.macaddress)
            self.printer_hardware = hardware.Paperang(config.macaddress)
        else:
            print("searching for printer for test print...")
            self.printer_hardware = hardware.Paperang()

        # having trouble connecting? uncomment the following line and input
        # your paperang's MAC address directly
        # self.printer_hardware = hardware.Paperang("AA:BB:CC:DD:EE:FF")

    def print_self_test(self):
        if self.printer_hardware.connected:
            self.printer_hardware.sendSelfTestToBt()
            self.printer_hardware.disconnect()
        else:
            print("printer not connected.")

    def print_image(self, path):
        if self.printer_hardware.connected:
            self.printer_hardware.sendImageToBt(image_data.im2binimage2(path))

if __name__ == '__main__':
    mmj=Paperangg_Printer()
    for imgPath in sys.argv[1:]:
    	mmj.print_image(imgPath)

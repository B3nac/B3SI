#Sensor Interface created by Kyle Benac

import sys
import subprocess
import time
import serial

print('B3SI version 1.0. Cmd line testing programmed in Python3')

class B3SI(object):

    def __init__(self):
        self.cmd = ''
        self.done = False

    #Mostly to test functions
    def event_loop(self):
        self.cmd = input('(B3)> ')

        if self.cmd == 'cpu_temp':
            self.check_temp()
        elif self.cmd == 'a_temp':
            self.a_temp()
        elif self.cmd == 'sort_uniq':
            self.sort_uniq()
        elif self.cmd == 'take_pic':
            self.take_pic()
        elif self.cmd =='help':
            print("Commands are cpu_temp, a_temp, sort_uniq, take_pic, exit")
        elif self.cmd == 'exit':
            self.exit_loop()
        else:
            print('Command does not exist,'
                  'try help for list of commands')

    def cmd_loop(self):
        while not self.done:
            self.event_loop()

    def a_temp(self):
        print("Atmosphere temp is: ")

        arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=.1)
        time.sleep(1) #give the connection a second to settle
        data = arduino.readline()
        line = 1
        if data:
            if line <= 1:
                print(data[:5])
                line += 1

    def sort_uniq(self):
       uniq = './sort_uniq.sh'
      # uniq = subprocess.Popen(['./', 'sort','log.txt', '|', 'uniq', '|', 'sponge', 'log.txt'], stdout = subprocess.PIPE)
       subprocess.call(uniq, shell = True)
       print("Sorted unique strings successfully!")

    def take_pic(self):
        pic = './take_pic.sh'
        subprocess.call(pic, shell = True)
        print("Taking pictures.")

    def check_temp(self):
        try:
            ctemp = subprocess.Popen(["/opt/vc/bin/vcgencmd","measure_temp"],stdout=subprocess.PIPE)
            output, err = ctemp.communicate()
            print("Current CPU temp: ")
            print(str(output.decode().rstrip()[5:]))
        except:
            print('Error: This command only works on Raspberry pi, is it an OS issue?')

    def exit_loop(self):
        self.done = True

def main():
	start = B3SI()
	start.event_loop()
	start.cmd_loop()


if __name__ == '__main__':
	main()

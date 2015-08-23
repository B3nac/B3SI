import os
import sys
import subprocess
import socket
import time
import locale
import serial

print('B3interface version 1.0. Using Python3')

class B3interface(object):
    
    def __init__(self):
        self.cmd = ''
        self.done = False

    def event_loop(self):
        self.cmd = input('(B3)> ')
			
        if self.cmd == 'listf':
            self.list_f()
        elif self.cmd == 'cpu_temp':
            self.check_temp()
        elif self.cmd == 'a_temp':
            self.a_temp() 
        elif self.cmd == 'netscan':
            self.network_scan()
        elif self.cmd == 'scan_ip':
            self.scan_ip(self)
        elif self.cmd == 'scan_os':
            self.scan_os()
        elif self.cmd == 'sort_uniq':
            self.sort_uniq()
        elif self.cmd == 'take_pic':
            self.take_pic()
        elif self.cmd == 'who':
            self.check_connections()
        elif self.cmd == 'exit':
            self.exit_loop()
            
        else:
            print('Command does not exist,'
	          'try help for list of commands')

    def cmd_loop(self):
        while not self.done:
            self.event_loop()
    
    def a_temp(self):
        log = open("log.txt", "a")
        print("Atmosphere temp is: ")
        
        arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
        time.sleep(1) #give the connection a second to settle
        data = arduino.readline()
        line = 1
        if data:
            if line < 10:
                print(data)
                line += 1
                log.write(str("\n"))
                log.write(str(data))
                log.close()

    def network_scan(self):
        print("Pinging network.")
        for ping in range(1,25):
            ip = '10.0.0.' + str(ping)
            encoding = locale.getdefaultlocale()[1]
            response = subprocess.Popen(['ping', '-c', '3', ip], stdout=subprocess.PIPE)
            output, err = response.communicate()
            
            connectip = socket.gethostbyname(ip)
           
            if 'Unreachable' in output.decode(encoding):
                print('pinging', ip, 'NOT CONNECTED')
            else:                       
                print('pinging', ip, 'CONNECTED!')
        
    def scan_os(self):

        encoding = locale.getdefaultlocale()[1]
        IP = subprocess.Popen(['nmap','-Pn', '--script','smb-os-discovery','-p 445','10.0.0.1/24'], stdout = subprocess.PIPE)
        log = open("log.txt", "a")
        for newlines in IP.stdout:
            columns = newlines.decode(encoding).split()
            if columns:
                print(columns[-1])
                log = open("log.txt", "a")
                log.write(str("\n"))
                log.write(str(columns))
                log.close()

    def sort_uniq(self):
       uniq = './sort_uniq.sh'       
      # uniq = subprocess.Popen(['./', 'sort','log.txt', '|', 'uniq', '|', 'sponge', 'log.txt'], stdout = subprocess.PIPE)
       subprocess.call(uniq, shell = True)
       print("Sorted unique strings successfully!")

    def scan_ip(router, self):
        print("Enter IP: ")
        router = input("")
        connectip = socket.gethostbyname(router)
        
        try:
            for port in range(1, 500):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((connectip, port))
                if result == 0:
                    print("Port {}: \t Open".format(port))
                    sock.close()
                else:
                    print("No ports open!")
                    
        except socket.error:
           print("Couldn't connect to ip.") 
  
    def take_pic(self):
        pic = './take_pic.sh'
        print("Taking pictures.")

    def check_connections(self):
        check = subprocess.Popen(["w"],stdout=subprocess.PIPE)
        output, err = check.communicate()
        print(output)

    def check_temp(self):
        try:
            ctemp = subprocess.Popen(["/opt/vc/bin/vcgencmd","measure_temp"],stdout=subprocess.PIPE)
            output, err = ctemp.communicate()
            print("Current CPU temp: ")
            print(str(output.decode().rstrip()[5:]))
        except:
            print('Error: This command only works on Raspberry pi, is it an OS issue?')

    def list_f(self):
        mypath = os.getcwd()
        print(os.listdir(mypath))
        
    def exit_loop(self):
        self.done = True
        
def main():
        start = B3interface()
        start.event_loop()
        start.cmd_loop()
	
if __name__ == '__main__':
	main()


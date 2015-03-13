#Autorun script created by Kyle Benac
import B3SI
from time import sleep

def main():
    done = False
    while not done:
        print(" ------------------------------------------- ")
        print(" |           Starting autopilot!           | ")
        print(" ------------------------------------------- ")
        auto = B3SI.B3()
        auto.check_temp()
        auto.a_temp()
        auto.take_pic()
        print(" -------------------------------------------------- ")
        print(" | Waiting a couple minutes before another loop.  | ")
        print(" -------------------------------------------------- ")
        sleep(200)
    
if __name__ == '__main__': 
        main()

#Autorun script created by Kyle Benac

import B3SI
from time import sleep

def main():
    print(" ------------------------------------------- ")
    print(" |           Starting autopilot!           | ")
    print(" ------------------------------------------- ")
    auto = B3SI.B3SI()
    auto.check_temp()
    auto.a_temp()
    auto.take_pic()
    auto.sort_uniq()
    print(" -------------------------------------------------- ")
    print(" | Waiting a couple minutes before another loop.| ")
    print(" -------------------------------------------------- ")
    sleep(200)
    main()

if __name__ == '__main__':
    main()

import B3
from time import sleep

def main():
    print(" ------------------------------------------- ")    
    print(" |           Starting autopilot!           | ")
    print(" ------------------------------------------- ")
    auto = B3.B3interface()
    
    auto.check_temp()
    auto.a_temp() 
    auto.sort_uniq()
    print(" -------------------------------------------------- ") 
    print(" | Waiting a couple minutes before another rescan.| ")
    print(" -------------------------------------------------- ")
    sleep(200)
    main()

if __name__ == '__main__':
    main()

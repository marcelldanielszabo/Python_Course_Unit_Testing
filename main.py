# This work is created by Szabo, Marcell Daniel (uie63187)
import sys, getopt


#------------------------------------------#
#-----------------FUNCTIONS----------------#
#------------------------------------------#

def Sum_Three_Fnc(arg1,arg2,arg3):
    value =  sum([arg1,arg2,arg3])
    return value
    
#------------------------------------------#
#--------------------MAIN------------------#
#------------------------------------------#


def main(): # Start of Function: Main
    print(Sum_Three_Fnc(1,2,3))
# End of function: Main

if __name__ == "__main__":
   main()
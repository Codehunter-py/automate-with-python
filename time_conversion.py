#!/usr/bin/python3

################################################################################
# Name    : time_conversion.py                                                 #
# Author  : Ibrahim Musayev                                                    #
# Purpose : Function does return a new string representing the input           #
#           time in 24 hour format.                                            #
# History : 28-01-22 : creation                                                #
################################################################################

def timeConversion(s):
   if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
   elif s[-2:] == "AM":
        return s[:-2]
   elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
   else:
        return str(int(s[:2]) + 12) + s[2:8]

if __name__ == '__main__':
    s = input("Enter time in 12 hour format I:M:S[AM|PM]: ")
    result = timeConversion(s)
    print(result)


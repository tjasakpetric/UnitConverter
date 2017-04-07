# -*- coding: utf-8 -*-
#Naloga: Pretvornik enot, pretvarja kilometre v milje in obratno. 

print "Hello! welcome to converter!"
print "You can convert kilometers to miles or miles to kilometers."

while True:
    option = raw_input("Type km-mi to convert kilometers to miles or mi-km to convert miles to kilometers: ").lower()
    if option == "km-mi":
        print "You are currently converting kilometers to miles."
        convert = raw_input("Enter a number in kilometers that you would like to convert to miles: ")
        try:
            km = float(convert) * 0.62
            print convert + " kilometers = " + str(km) + " miles"
        except ValueError:
            print "Enter only numbers please!"


    elif option == "mi-km":
        print "You are currently converting miles to kilometers."
        convert = raw_input("Enter a number in miles that you would like to convert to kilometers: ")
        try:
            m = float(convert) / 0.62
            print convert + " miles = " + str(m) + " kilometers"
        except ValueError:
            print "Enter only numbers please!"

    again = raw_input("If you want to convert some more type Y, or type N to exit the converter: ").lower()
    if again == "y":
        pass
    elif again == "n":
        break

print "Thank you for using this converter."

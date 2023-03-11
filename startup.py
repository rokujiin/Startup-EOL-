import os
import time
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")




print('Welcome back, Rey!')
print('')
print("Today's date is: ", dt_string)
print('')
start = input("Would you like to start your overlay, y or n? ")




#whileuser input is not y or n, keep asking

while start != "y"  and start != "n" and start != "Y" and start != "N":
    start = input("Please enter y or n: ")
    
if start == "n" or start == "N":
    exit()
    
elif start == "y" or start == "Y":   
    print("Overlay starting in: ")
        
    countdown = 3
    while countdown > 0:
        print(countdown)
        countdown = countdown - 1
        time.sleep(1)
                   
        if countdown == 0:
            response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
            print(response)
            response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
            print(response)
            response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\IntelliJ IDEA 2022.2.3.lnk")
            print(response)
            response = os.startfile(r"H:\IDEs\Microsoft VS Code\bin\code.cmd")
            print(response)
            response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\HWiNFO64\HWiNFO64.lnk")
            print(response)
            response = os.startfile(r"C:\Users\rheyp\Desktop\Discord.lnk")
            print(response)
          
            break
            

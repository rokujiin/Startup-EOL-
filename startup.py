import os
import time


print('Welcome back, Rey')
print('')
start = input("Would you like to start your overlay, y or n? ")
if start == "n":
    exit()
elif start == "y":   
    print("Overlay starting in: ")
        
    countdown = 6
    while countdown > 0:
        time.sleep(1)
        countdown = countdown - 1
        print(countdown)
            
        if countdown == 0:
            response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
            print(response)

            response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
            print(response)
            
            response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\IntelliJ IDEA 2022.2.1.lnk")
            print(response)

            response = os.startfile(r"H:\IDEs\Microsoft VS Code\bin\code.cmd")
            print(response)

            response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\HWiNFO64\HWiNFO64.lnk")
            print(response)

            response = os.startfile(r"C:\Users\rheyp\Desktop\Discord.lnk")
            print(response)
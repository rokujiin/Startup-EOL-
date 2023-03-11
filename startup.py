import os
import time

class Startup:

    def __init__(self):
        self.name = "Rey"
        self.start()

    def start(self):
        print("Welcome back, " + self.name + "!")
        print("")
        print("The time is: " + time.strftime("%H:%M:%S"))
        print("")
        self.overlay()
    
        
    def overlay(self):
        start = input("Would you like to start your overlay, y or n? ")
        while start != "y" and start != "n":
            start = input("Would you like to start your overlay, y or n? ")
        if start == "n":
            exit()
        elif start == "y":
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
                
if __name__ == "__main__":
    Startup()
    

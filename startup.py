import os
import time

class Startup:

    def __init__(self):
        self.ampm = time.strftime("%p")
        self.name = "Rey"
        self.start()

    def start(self):
        print("Welcome back, " + self.name + "!")
        print("")
        print("Your system started at " + time.strftime("%A %B %d, %Y")+ " " + time.strftime("%H:%M:%S") + " " + self.ampm)
        print("")
        self.overlay()
    
    def overlay(self):
        start = input("Would you like to start your overlay, y or n? ")
        while start != "y" and start != "n":
            start = input("Would you like to start your overlay, y or n? ")
        if start == "n":
            exit()
        elif start == "y":
            print("Gotcha! ")
            print("Starting overlay in: ")
            countdown = 3
            while countdown > 0:
                print(countdown)
                countdown = countdown - 1
                time.sleep(1)
                if countdown == 0:
                    try:
                        with open("I:/CodeProjects/Python/Startup/app_list.txt", 'r') as file:
                            apps = file.readlines()
                    except FileNotFoundError:
                        print("File not found!")
                        exit()

                    for app in apps:
                        app = app.strip()
                        os.startfile(app)
if __name__ == "__main__":
    Startup()
    

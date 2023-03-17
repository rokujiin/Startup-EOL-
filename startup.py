import os
import time


class Startup:
    def __init__(self):
        self.ampm = time.strftime("%p")
        self.name = "Rey"
        self.start()

    def start(self):
        print(f"Welcome back, {self.name}!")
        print("")
        print(f"Your system started at {time.strftime('%A %B %d, %Y')} {time.strftime('%H:%M:%S')} {self.ampm}")
        print("")
        self.overlay()

    def overlay(self):
        start = input("Would you like to start your overlay, y or n? ")
        while start not in ["y", "n"]:
            start = input("Would you like to start your overlay, y or n? ")
        if start == "n":
            exit()
        elif start == "y":
            print("Gotcha!")
            print("Starting overlay in:")
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)
            try:
                with open("I:/CodeProjects/Python/Startup/app_list.txt", "r") as file:
                    apps = file.readlines()
            except FileNotFoundError:
                print("File not found!")
                exit()

            for app in apps:
                app = app.strip()
                try:
                    os.startfile(app)
                except OSError:
                    print(f"Failed to open {app}")

if __name__ == "__main__":
    Startup()

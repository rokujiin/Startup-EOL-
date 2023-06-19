import os
import time

class OverlayStarter:
    def __init__(self):
        print("Welcome back, Rey\n")

    def start_overlay(self):
        while True:
            start = input("Would you like to start your overlay? (y/n): ")
            if start == "n":
                exit()
            elif start == "y":
                break

    def choose_application(self):
        while True:
            start1 = input("Start IntelliJ or VS Code with Chrome? (intellij/vscode): ")
            if start1 == "intellij":
                overlay_path = r"C:\Program Files (x86)\JetBrains\IntelliJ IDEA 2022.2.3\bin\idea64.exe"
                break
            elif start1 == "vscode":
                overlay_path = r"C:\Users\Rey Halili\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk"
                break

        chrome_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
        return overlay_path, chrome_path

    def start_countdown(self):
        print("\nOverlay starting in:")
        try:
            for countdown in range(3, 0, -1):
                print(countdown)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program canceled")
            exit()

    def start_applications(self, overlay_path, chrome_path):
        response = os.startfile(overlay_path)
        print(response)

        response = os.startfile(chrome_path)
        print(response)

if __name__ == "__main__":
    overlay_starter = OverlayStarter()
    overlay_starter.start_overlay()
    overlay_path, chrome_path = overlay_starter.choose_application()
    overlay_starter.start_countdown()
    overlay_starter.start_applications(overlay_path, chrome_path)


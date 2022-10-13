import os
import time
from tracemalloc import start
from urllib import response
from xmlrpc.client import ResponseError

print("Welcome back Rey")
print("")

start = input("Would you like to start your overlay, y or n? ")
if start == "n":
  exit()
  

elif start == "y":
        
    start1 = input("Start intellij or vscode with Chrome? ")
    if start1 == "vscode":
            
        print ("Overlay starting in:")
        countdown = 5
        while countdown > 0:
            print (countdown)
            countdown = countdown - 1
            time.sleep(1)
            if countdown == 0:
                    
                    response = os.startfile(r"C:\Users\Rey Halili\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
                    print(response)
               
                    response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
                    print(response)
                    

    elif start1 == "intellij":
                
        print ("Overlay starting in:")
        countdown = 5
        while countdown > 0:
            print (countdown)
            countdown = countdown - 1
            time.sleep(1)
            if countdown == 0:
                        
                response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\IntelliJ IDEA 2022.2.1.lnk")
                print(response)
                        
                response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
                print(response)

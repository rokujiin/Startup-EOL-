import os
import time
from tracemalloc import start
from urllib import response

print("Welcome back Rey")
print("")


start = input("Would you like to start your overlay, y or n? ")

#while user input is not equal to y or n, keep asking
while start != "y" and start != "n":
    start = input("Would you like to start your overlay, y or n? ")
    
if start == "n":
  exit()
  

elif start == "y":
    
   
    start1 = input("Start intellij or vscode with Chrome? ")
    
    #while user input is not equal to intellij or vscode, keep asking
    while start1 != "intellij" and start1 != "vscode":
        start1 = input("Start intellij or vscode with Chrome? ")
        
    if start1 == "vscode": #vscode path
                
        print ("Overlay starting in:")
        countdown = 3  
        while countdown > 0:
            print (countdown)
            countdown = countdown - 1
            time.sleep(1)
            if countdown == 0:
                        
                response = os.startfile(r"C:\Users\Rey Halili\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
                print(response)
            
                response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
                print(response)
                    

    elif start1 == "intellij": #intellij path
                
        print ("Overlay starting in:")
        countdown = 3
        while countdown > 0:
            print (countdown)
            countdown = countdown - 1
            time.sleep(1)
            if countdown == 0:
                        
                response = os.startfile(r"C:\Program Files (x86)\JetBrains\IntelliJ IDEA 2022.2.3\bin\idea64.exe")
                print(response)
                        
                response = os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
                print(response)

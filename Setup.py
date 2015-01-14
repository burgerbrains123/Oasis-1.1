import os
import winsound
import time

print ("Hello and welcome to Oasis 1.1 (Alpha)")
os.system("pause")
os.system("color 17")
os.system("cls")
print("Installation step 1")
os.system("pause")
name = (input("What is your Prefered Name? "))

os.system("cd\")
os.system("mkdir Oasis")
os.system("cd Oasis")
os.system("mkdir FTIF") #FTIF means first time installation files
os.system("cd FTIF")

file = open("c/Oasis/FTIF/ netuser.bat", "w")
file.write("@echo off" + "\n" + "color 17" + "\n" + "cls" + "\n" + "echo Here is a list of users" + "\n" + "echo." + "\n" + "netuser" + "\n" + "pause" + "\n" + "exit")
file.close()
os.system("start netuser.bat")

print ("Stop " + name + "! dont close the program that just came up. it has a list")
print ("of users on this computer please type in your Username exactly as")
print ("it is spelt in the list")
USER = (input(": "))
os.system("pause")
print("Installation step 2 (creating Dump File)")

os.system("cd..")
os.system("mkdir Dump_Files")

file = open("c/Oasis/Dump_Files/ Preferred_Name_and_UserName.txt", "w")
file.write(name + "\n" + USER + "\n")
file.close()

print("Installation step 2 (creating shortcuts)")

DESKTOP_PATH = ("c/Users/" + USER + "/Desktop/ ")

os.system("cd\")
os.system("cd Oasis")
os.system("mkdir Main")
file = open(DESKTOP_PATH + "Oasis.bat", "w")
file.write("@echo off" + "\n" + "color 17" + "\n" + "cls" + "\n" + "cd.." + "\n" + "cd.." + "\n" + "cd.." + "\n" + "cd.." + "\n" + "cd Oasis" + "\n" + "cd Main" + "\n" + "start Main.py")
file.close()

print ("Installation step 3 (Setting up main program.)")

os.system("cd\")
os.system("cd Oasis")
os.system("mkdir Main")
file = open("c/Oasis/Main/ Main.py")
file.write("import os" + "\n" + "os.system("color 17")" + "\n" + "COMMAND = (input("enter command: "))" + "\n" + "if COMMAND==OD:" + "\n" + "    os.system("start OD.py")" + "\n" + "if COMMAND==SC:" + "\n" + "    os.system("start cmd.exe")" + "\n" + "if COMMAND==SN:" + "\n" + "    os.system("start notepad.exe")" + "\n" + "if COMMAND==CP:" + "\n" + "    os.system("start CP.py")" + "\n" + "if CCOMMAND==MUP:" + "\n" + "    os.system("start MUP.py")" + "\n" + "if COMMAND==CUPN:" + "\n" + "    os.system("start CUPN.py")" + "\n" + "os.system("pause")" + "\n" + "if COMMAND==exit:" + "\n" + "    os.system("exit")" + "\n" + "print("invalid choice")" + "\n" + "os.system("pause")" + "\n" + "os.system("start Main.py")" + "\n" + "os.system("exit")")
file.close()

file = open ("OD.py", "w")
file.write("import os" + "\n" + "os.system("color 17"))

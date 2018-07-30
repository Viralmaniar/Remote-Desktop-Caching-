#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This tool allows one to recover old RDP (mstsc) session information in the form of broken PNG files. These PNG files allows Red Team member to extract juicy information such as LAPS passwords or any sensitive information on the screen. Blue Team member can reconstruct PNG files to see what an attacker did on a compromised host. It is extremely useful for a forensics team to extract timestamps after an attack on a host to collect evidences and perform further analysis.

Special thanks to Paula Januszkiewicz and Greg Tworek from CQURE - https://www.youtube.com/watch?v=KufLD-ByuLU

Author: Viral Maniar 
Twitter: https://twitter.com/maniarviral
Github: https://github.com/Viralmaniar
LinkedIn: https://au.linkedin.com/in/viralmaniar
'''
import os, sys
from pathlib import Path
import subprocess
from subprocess import check_output
import argparse

def logo():
	logo = '''
                                    __________
                           ________|          |________
                          |       /   ||||||   \       |
                          |     ,'              `.     |
                          |   ,'                  `.   |
                          | ,'   ||||||||||||||||   `. |
                          ,'  /____________________\  `.
                         /______________________________\
						 
			|                                |
                        |      Remote Desktop Caching    |
			|       Author: Viral Maniar     |
			|       Twitter: @ManiarViral    |
                        |________________________________|
                          |____________________------__|
[+] Description: This tool allows one to recover old RDP (mstsc) session information in the form of broken PNG files. These PNG files allows Red Team member to extract juicy information such as LAPS passwords or any sensitive information on the screen. Blue Team member can reconstruct PNG files to see what an attacker did on a compromised host. It is extremely useful for a forensics team to extract timestamps after an attack on a host to collect evidences and perform further analysis.
[+] Python version: 3.6.3
[+] PowerShell version: 5.1
'''
	return logo
	
OPTIONS = '''
1. Get Execution Policy of Current Session
2. Set Execution Policy to Bypass
3. List RDP Sessions Cached Files
4. Extract Sensitve Information from previous RDP Sessions
5. Exit

'''
def menu():
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? \n> ')).lower()
			if choice[0] == 'y':
				return
			if choice[0] == 'n':
				sys.exit(0)
				break
		except ValueError:
			sys.exit(0)

def checkHostWindows():
	if os.name == "nt":
		print ('[+] All good....')
	else:
		print ('[!] Please run the application on Windows machine')
		sys.exit(0)

def cmd_getExectionPolicy():

	process=subprocess.Popen(["powershell","Get-ExecutionPolicy"], shell=False);
	result=process.communicate()[0]
	print(result)

def cmd_exectionPolicy():

	process=subprocess.Popen(["powershell","Set-ExecutionPolicy -Scope CurrentUser bypass"], shell=False);
	result1=process.communicate()[0]
	print(result1)
	print ("Execution policy is now set to bypass.")
	
def cmd_getCachedFiles():
	process=subprocess.Popen(["powershell","Get-ChildItem \"$env:LOCALAPPDATA\Microsoft\Terminal Server Client\Cache\""], shell=False);
	result3=process.communicate()[0]
	print(result3)
	print ("All cached files listed")
	

def cmd_remoteCache():

	process=subprocess.Popen(["powershell","rdpcache.ps1"], shell=False);
	result2=process.communicate()[0]
	print(result2)
	print ("Successfully reconstructed sensitve information from previous RDP sessions.")
	
cmds = {
	"1" : cmd_getExectionPolicy,
	"2" : cmd_exectionPolicy,
	"3" : cmd_getCachedFiles,
	"4" : cmd_remoteCache,
	"5" : lambda: sys.exit(0)
}

def main():
	os.system('cls')
	print (logo())
	checkHostWindows()
	try:
		while True:
			choice = input("\n%s" % OPTIONS)
			if choice not in cmds:
				print ('[!] Invalid Choice')
				continue
			cmds.get(choice)()
	except KeyboardInterrupt:
		print ('[!] Ctrl + C detected\n[!] Exiting')
		sys.exit(0)
	except EOFError:
		print ('[!] Ctrl + D detected\n[!] Exiting')
		sys.exit(0)

if __name__ == "__main__":
	main()

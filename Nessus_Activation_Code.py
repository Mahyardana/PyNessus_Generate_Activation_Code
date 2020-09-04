from bs4 import BeautifulSoup
import requests
import time
import re
from mohmal import Mohmal
import os
import sys
import argparse

def banner():
	print("==================================================================")
	print("            Generate Multiple Nessus Activation code                       ")
	print("   Don't misuse this script other then for Pentesting purpose              ")
	print("                      \033[1;31;10mBy:Fools of Security :)\033[1;31;0m     ")
	print("==================================================================")


def nessus_activation(firstname,lastname):
	tmp = Mohmal()
	email = tmp.Get_Random_Email() 
	print("Your Temp mail address is successfully created!")
	print ("Email Address: "+ email)
	# print tmp.get_mailbox(email)  
	#Nessus Registeration Form
	print ("\033[1;32;10mNessus Registeration Form \033[1;32;0m")
	ht=requests.get("https://www.tenable.com/products/nessus-home")
	bs=BeautifulSoup(ht.text,'html.parser')
	for link in bs.findAll("input",{"name":"token"}):
	 if 'name' in link.attrs:
	   tkn=link.attrs['value']
	 else:
	   print("not found")
	fname=firstname
	lname=lastname
	# nes_email=raw_input("Email:")
	params={"first_name":fname,"last_name":lname,"email":email,"country":"NL","robot":"human","type":"homefeed","token":tkn,"submit":"Register"}
	r = requests.post("https://www.tenable.com/products/nessus/nessus-essentials", data=params)
	if r.status_code == 200:
		bs=BeautifulSoup(r.text,'html.parser')
		keyword=bs.find("title").get_text()
		success=keyword.split('|')
		if str(success[0][:-1]) == 'Thank You for Registering for Nessus Essentials!':
			print('\033[1;32;10m'+str(success[0][:-1])+'\033[1;32;0m')
			while  True:
				mail=tmp.get_mailbox("Tenable Nessus Essentials Activation Code")
				if mail is not None:
					message=tmp.read_mail(mail)
					regex = r"\w{4}(?:-\w{4}){4}"
					activation_code=re.search(regex,message)
					print('\033[1;32;10mNessus Activation Code is:\033[1;32;0m'+activation_code.group())
					sys.exit()
				else:
					print ('There are no emails yet....')

		elif bs.find('span',{"style":"color:#FF0000;"}).get_text():
			os.system('clear')
			# print('\033[1;31;10m'+bs.find('span',{"style":"color:#FF0000;"}).get_text()+'\033[1;31;0m')
			print('\033[1;31;10m Sorry, This Email Address is already Registered for Nessus Activation Code\033[1;31;0m')
			print("Wait..Regenerating new Temp email address")
			nessus_activation()
	else:
		print("something went wrong with the request")
		sys.exit()

parser=argparse.ArgumentParser()
parser.add_argument("-f","--firstname",help="FirstName")
parser.add_argument("-l","--lastname",help="LastName")


if __name__ == "__main__":
	args=parser.parse_args()
	banner()
	if False and args.firstname is None and args.lastname is None:
		parser.print_help()
	else:
		nessus_activation(args.firstname,args.lastname)


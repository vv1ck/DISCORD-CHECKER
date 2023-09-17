from requests import post,get
import base64,os,requests,json
from random import choice
from threading import Lock,Thread
from time import sleep
red = "\033[1;31;40m";yel = '\033[1;33;40m';grn = '\033[1;32;40m';wit = "\033[1;37;40m";bloFT = "\033[1;36;40m"

class DISCORD_CHECKER:
	def __init__(self,DV,Modes):
		self.PRNT=Lock()
		self.STR=True
		self.CompLst=[]
		self.proxylist = []
		self.theards =[]
		self.DV=DV;self.Modes=Modes;self.COM=0
		self.DN,self.NO,self.ERR,self.PRX=0,0,0,0
		try:self.Telegrams=open('TeleToken.txt','r').readline().split('\n')[0].split('<')
		except FileNotFoundError:
			self.Telegrams='vv1ck'
		self.trts()
	
	def HEADERS(self):
		return {"x-debug-options" : "bugReporterEnabled","Content-Type" : "application/json","User-Agent" : "Discord/47806 CFNetwork/1126 Darwin/19.5.0","Content-Length" : "19","Accept-Language" : "ar-JO,en-JO;q=0.9","Connection" : "keep-alive","Host" : "discord.com","Accept" : "*/*","x-super-properties": str(base64.b64encode(str('{"os":"iOS","browser":"Discord iOS","device":"iPhone8,1","system_locale":"ar-JO","client_version":"191.0","release_channel":"stable","device_vendor_id":'+str(choice(['iPhone8,1','iPhone8,4','iPhone10,1','iPhone11,2','iPhone14,5','iPhone13,3','iPhone15,2','iPhone15,3','iPhone14,4']))+',"system_locale":"ar-JO","client_version":"191.0","release_channel":"stable","device_vendor_id":'+str("".join((choice("R74E7A3E10D2DFCAA18V") for i in range(8))))+"-"+str("".join((choice("R74E7A3E10D2DFCAA18V") for i in range(4))))+"-"+str("".join((choice("R74E7A3E10D2DFCAA18V") for i in range(4))))+"-"+str("".join((choice("R74E7A3E10D2DFCAA18V") for i in range(17))))+',"browser_user_agent":"","browser_version":"","os_version":"13.5","client_build_number":48396,"client_event_source":null,"design_id":0}').encode("utf-8"))).split("b'")[1].split("'")[0],"x-discord-locale" : "en-US","x-discord-timezone" : "Asia/Amman"}

	
	def START_CHACKER(self):
		while self.STR:
			if self.Mod=='File':
				if self.COM == len(self.CompLst):
					self.STR=False
					print('\n Examination finished..\n')
					sleep(10)
					exit()
				else:
					user=self.CompLst[self.COM]
			else:
				user=str("".join((choice("qazwsx123edcrfv456tgbyh_n789ujmikl0") for i in range(self.ch))))
			
			try:
				run = str(choice(self.proxylist))
				VV1ck=post('https://discord.com/api/v9/unique-username/username-attempt-unauthed',headers=self.HEADERS(),json={"username":user},proxies= {"http": f"http://{run}","https": f"http://{run}"})
				if VV1ck.text.__contains__('"taken":true'):
					self.NO+=1
				elif VV1ck.text.__contains__('"taken":false'):
					self.DN+=1
					with open('New_discord.txt', 'a') as J:J.write(user+'\n')
					post(f'https://api.telegram.org/bot{self.Telegrams[1]}/sendPhoto?chat_id={self.Telegrams[0]}&caption=👾 discord User :\n➖ [ {user} ] ➖\nBy @vv1ck',files={'photo': get('https://k.top4top.io/p_2814c924v0.jpeg').content})
				elif VV1ck.text.__contains__('"message": "The resource is being rate limited."'):
					self.PRX+=1

				else:
					print(VV1ck.text)
			except KeyboardInterrupt:
				self.STR=False
				sleep(10)
				sys.exit()
			except requests.exceptions.ConnectionError:
				self.PRX+=1
			except requests.exceptions.ReadTimeout:
				self.PRX+=1

			if self.STR==False:
				sleep(10)
				exit()
			if DV=='pc':
				print(f'\r{grn}DONE: {self.DN} {wit}| {red}Not available: {self.NO} {wit}| {yel}Proxys:{self.PRX}{wit}\r',end="")
			else:
				print(f'\rDONE: {self.DN} | Not available: {self.NO} | Proxys:{self.PRX}\r',end="")
			self.COM+=1
	
	def returns(self):
		if self.DV=='pc':print(f"\n{bloFT}┌──(joker㉿root)-[{wit}~{red}DISCORD-CHECKER.exe{red}{bloFT}]\n└─${wit} The file name is incorrect !\n")
		else:print('\n┌──(joker㉿root)-[~DISCORD-CHECKER.exe]\n└─$ The file name is incorrect !\n')
	def trts(self):
		if self.Modes=='1':
			self.Mod='File'
			try:
				for J in open(input('₿:~ Enter Users File: '),'r').read().splitlines():
					self.CompLst.append(J)
				
				if len(self.CompLst)>=150:
					tr=200
				elif len(self.CompLst)<=100:
					tr = 50
				else:
					tr = 100
			except FileNotFoundError:
				self.returns();return self.trts()
		else:
			self.Mod='random'
			try:
				self.ch=int(input('₿:~ Enter the length username [ 3 / 4 / 5 ]: '))
				tr=200
			except ValueError:print('Please enter a number, not a letter !');return self.trts()
		
		try:
			for J in open(input('₿:~ Enter Proxy File: '),'r').read().splitlines():
				self.proxylist.append(J)
		except FileNotFoundError:
			self.returns();return self.trts()
		
		if self.DV=='pc':print(f"{bloFT}┌──(joker㉿root)-[{wit}~{red}DISCORD-CHECKER.exe{red}{bloFT}]\n└─${wit} :")
		else:print('┌──(joker㉿root)-[~DISCORD-CHECKER.exe]\n└─$ :')
		#Thread(target=self.PRINTS).start()
		print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
		for i in range(tr):
			trts=Thread(target=self.START_CHACKER)
			trts.start()
			self.theards.append(trts)
		for trts2 in self.theards:
			trts2.join()
		input('Done')

if __name__ == '__main__':
	OS = input("┌──(joker㉿root)-[~DISCORD-CHECKER.exe]\n└─$ What are you using ? \n\t\t[1] PC / rdp\n\t\t[2] mobile :")
	if OS == '1':DV='pc';os.system("cls" if os.name=='nt' else "clear");Modes = input(f"{bloFT}┌──(joker㉿root)-[{wit}~{red}DISCORD-CHECKER.exe{red}{bloFT}]\n└─${wit} {yel}Modes{wit} :\n\t 1- Checking usernames from a file\n\t 2- Automatic checker\n->> Choose the mode: ")
	else:DV='me';os.system('clear');Modes = input(f"┌──(joker㉿root)-[~DISCORD-CHECKER.exe]\n└─$Modes :\n\t 1- Checking usernames from a file\n\t 2- Automatic checker\n->> Choose the mode: ")
	try:open('TeleToken.txt','r')
	except FileNotFoundError:
		Telegram=input('₿:~ Want to send your catch on Telegram? [ y / n ]')
		if Telegram=='y'or'Y':
			ID = input('₿:~Enter You ID : ')
			token = input('₿:~Enter Token Bot: ')
			with open('TeleToken.txt', 'a') as J:J.write(f'{ID}<{token}\n')
		else:pass
	DISCORD_CHECKER(DV,Modes)

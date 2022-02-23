###Don't copy, take a look and try it yourself###
import requests, os

os.system("clear")
def intro():
  fuck = ("\033[1m\033[32mURL SHORTNER BY TOXIC-VIRUS\nGithub : https://github.com/TXVIRUS\nTelegram : httls://t.me/txvirus\nSite : http://txvirus.akxvau.ml\nFacebook : https://www.facebook.com/t0xicvirus\nMohammad Alamin: https://www.facebook.com/t0xicvirus\033[0m")
  print(fuck)
  print("")
intro()
inp = str (input("\033[36mEnter Your Url : \033[37m"))
os.system("clear")
print ("Your Url : "+inp+"\n")
url =("http://tinyurl.com/api-create.php?url="+inp)
urlx = requests.get(url).text
if urlx == "Error":
	os.system("python url.py")
else:
	print ("\033[36m\nShorten Url : \033[37m"+urlx)
restart = ""
restartx = input("\033[31mPress any key for restart !")
###Tool Restart###
if restartx==restart:
	os.system("python url.py")
else:
	os.system("python url.py")

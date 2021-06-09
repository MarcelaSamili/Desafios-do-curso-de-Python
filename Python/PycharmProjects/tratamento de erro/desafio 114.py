import urllib
from urllib import request

try:
    site = urllib.request.urlopen('http://www.youtube.com')
except:
    print('\033[31mO site YouTube nao está acessivel no momento :(!\033[m')
else:
    print('\033[32mConsegui acessar o\033[m \033[31mYouTube\033[m \033[32mnorlmente!\033[m')
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.facebook.com/?ref=tn_tnmn')
except urllib.request.URLError:
    print('\033[0;31mO site não está acessivel no momento!\033[m')
else:
    print('\033[0;32mO site está acessive no momento!\033[m')
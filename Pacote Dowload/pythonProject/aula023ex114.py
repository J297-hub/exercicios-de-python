import urllib
import urllib.request
try:
    site= urllib.request.urlopen('https://www.google.com.br')
except:
    print('deu erro')
else:
    print('tudo ok')
    print(site.read())


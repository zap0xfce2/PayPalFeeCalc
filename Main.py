from bs4 import BeautifulSoup
import requests
import sys
import Console

if len(sys.argv) <= 1:
    Console.error('Es muss ein Argument übergeben werden!')
    Console.info('1.) Restbetrag der über bleiben soll')
    Console.info('Beispielaufruf: ' + sys.argv[0] + ' 32\n')
    sys.exit()
else:
    MoneyBack = float(sys.argv[1].replace(',', '.'))

URL = 'https://www.online-gebuehrenrechner.de/paypal.php'
RequestData = {'sales2': MoneyBack, 'submitbutton': 'Berechnen'}
RequestPost = requests.post(URL, data=RequestData)
soup = BeautifulSoup(RequestPost.text, 'html.parser')
HTML_Tags = soup.find_all(class_="paypal1")
Result = HTML_Tags[1].string[:-3].strip()
# Rückgabe für die Shell
#print(Result + "€")
# Rückgabe für Alfred App
print('<?xml version = "1.0"?><items><item uid = "1" arg = "' + Result + '€"><title>' + Result + '€</title><subtitle>Müssen vom Käufer gezahlt werden.</subtitle><icon>icon.png</icon></item></items>')

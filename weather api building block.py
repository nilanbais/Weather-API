"""
Voor info API, zie:
https://rapidapi.com/visual-crossing-corporation-visual-crossing-corporation-default/api/visual-crossing-weather/endpoints
"""
import requests
from datetime import datetime

# De aan te passen variabelen in het standaard blok
Datum = "01-01-2019"
Locatie = "Rotterdam"

# Omvormen van de datum naar het correcte voormat voor in de querystring voor de API
dateObject = datetime.strptime(Datum, "%d-%m-%Y").strftime('%Y-%m-%d')

# Vastleggen van de url
url = 'https://visual-crossing-weather.p.rapidapi.com/history'

# Definiëren van de querystring
querystring = {"dayStartTime": "8:00:00",
               "contentType": "csv",
               "dayEndTime": "17:00:00",
               "shortColumnNames": "false",
               "startDateTime": f'{dateObject}T00:00:00',
               "aggregateHours": "24",
               "location": f'{Locatie.capitalize()}%2C NL',  # NL kan vast, geen projecten buiten NL
               "endDateTime": f'{dateObject}T00:00:00',
               "unitGroup": "metric"}

# Definiëren van de headers
headers = {'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
           'x-rapidapi-key': "01760723f2msh9ad74e49c3fa409p14af2fjsn481f178a56b5"}

# De API bevragen
response = requests.request("GET", url, headers=headers, params=querystring)

# De response van de API manipuleren (kolommen en waarden splitsen)
r = response.text.split('\n')
par_names = r[0].split(',')
par_val = r[1].replace('"', '').split(',')

# De kolomnamen aan de juiste waarden kopellen
weerdata = dict()
for i in range(len(par_names)):
    weerdata[par_names[i]] = par_val[i]

# Statische variabele voor in de {} van de onderstaande f-string
datum = 'Date time'
temperatuur = 'Temperature'

# Printen van een resultaat
print(f'Op {weerdata[datum]} was het {weerdata[temperatuur]} graden Celsius in {Locatie}')

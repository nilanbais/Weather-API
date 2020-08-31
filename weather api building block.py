"""
Voor info API, zie:
https://rapidapi.com/visual-crossing-corporation-visual-crossing-corporation-default/api/visual-crossing-weather/endpoints
"""
from datetime import datetime

import pandas as pd
import requests
from pandas.io.json import json_normalize

# De aan te passen variabelen in het standaard blok
Datum = "01-01-2019"
Locatie = "Rotterdam"

# Omvormen van de datum naar het correcte voormat voor in de querystring voor de API
dateObject = datetime.strptime(Datum, "%d-%m-%Y").strftime('%Y-%m-%d')

# Vastleggen van de url
url = 'https://visual-crossing-weather.p.rapidapi.com/history'

# Definiëren van de querystring
querystring = {"dayStartTime": "8:00:00",
               "contentType": "json",
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
r = response.json()
df = json_normalize(r)

# Isoleren van de pd.Series met de waarden
df2 = df[f'locations.{Locatie.capitalize()}%2C NL.values']

# Isoleren van de dict met waarden uit de pd.Series
_d = df2.values
d = _d[0][0]

# Definiëren van de gewenste waarden
temp = d['temp']
mint = d['mint']
maxt = d['maxt']
humidity = d['humidity']
condition = d['conditions']

# Genereren van één dataframe met de gewenste waarden
weerdata = pd.DataFrame([{temp, mint, maxt, humidity, condition}],
                        columns=['temp', 'min temp', 'max temp', 'humidity', 'condition'])

# Printen om het resultaat te presenteren
print(weerdata)

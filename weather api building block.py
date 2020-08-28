import requests
from datetime import datetime


Datum = "01-01-2019"
Locatie = "Rotterdam"

url = 'https://visual-crossing-weather.p.rapidapi.com/history'

dateObject = datetime.strptime(Datum, "%d-%m-%Y").strftime('%Y-%m-%d')

querystring = {"dayStartTime": "8:00:00",
               "contentType": "csv",
               "dayEndTime": "17:00:00",
               "shortColumnNames": "false",
               "startDateTime": f'{dateObject}T00:00:00',
               "aggregateHours": "24",
               "location": f'{Locatie.capitalize()}%2C NL',  # NL kan vast, geen projecten buiten NL
               "endDateTime": f'{dateObject}T00:00:00',
               "unitGroup": "metric"}

headers = {'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
           'x-rapidapi-key': "01760723f2msh9ad74e49c3fa409p14af2fjsn481f178a56b5"}

response = requests.request("GET", url, headers=headers, params=querystring)

r = response.text.split('\n')
par_names = r[0].split(',')
par_val = r[1].replace('"', '').split(',')

weerdata = dict()
for i in range(len(par_names)):
    weerdata[par_names[i]] = par_val[i]

datum = 'Date time'
temperatuur = 'Temperature'

print(f'Op {weerdata[datum]} was het {weerdata[temperatuur]} graden Celsius in {Locatie}')

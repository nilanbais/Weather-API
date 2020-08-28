import requests
from datetime import datetime

url = 'https://visual-crossing-weather.p.rapidapi.com/history'

dayStartTime = "8:00:00"
dayEndTime = "17:00:00"
startDateTime = "01-01-2019"
endDateTime = startDateTime  # Gegeven van 1 dag. pas deze aan vor gegevens over interval van dagen
location = "Rotterdam"
contentType = "csv"  # Output format van de ontvangen data

dateObject = datetime.strptime(startDateTime, "%d-%m-%Y").strftime('%Y-%m-%d')

querystring = {"dayStartTime": dayStartTime,
               "contentType": contentType,
               "dayEndTime": dayEndTime,
               "shortColumnNames": "false",
               "startDateTime": f'{dateObject}T00:00:00',
               "aggregateHours": "24",
               "location": f'{location.capitalize()}%2C NL',  # NL kan vast, geen projecten buiten NL
               "endDateTime": f'{dateObject}T00:00:00',
               "unitGroup": "metric"}

headers = {'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
           'x-rapidapi-key': "01760723f2msh9ad74e49c3fa409p14af2fjsn481f178a56b5"}

response = requests.request("GET", url, headers=headers, params=querystring)

r = response.text.split('\n')

print(r)

par_names = r[0].split(',')
par_val = r[1].replace('"', '').split(',')

print(par_names)
print(len(par_names))
print(par_val)
print(len(par_val))

data = dict()
for i in range(len(par_names)):
    data[par_names[i]] = par_val[i]

print(data['Temperature'])

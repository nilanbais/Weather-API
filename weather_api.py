"""
Class for getting info from the weather api

Class should:
    [] - get location based on system info
    [] - make a request to the api to receive the data.
    [] - (optional) get input for preferences of data that is wished to be received
    [] - get the specified specs of the weather or give a filtered version of the received json
"""

from datetime import datetime


class WeatherApi:

    # Class variables
    _api_url = 'https://visual-crossing-weather.p.rapidapi.com/history'

    def __init__(self):
        self.date_today = datetime.today()
        self.date_object = None

        self.headers = {'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
                        'x-rapidapi-key': "01760723f2msh9ad74e49c3fa409p14af2fjsn481f178a56b5"}

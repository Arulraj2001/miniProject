import requests
import os
import datetime

def currentAstronomyData(latitude, longitude):
    api_key = '7f92c3823252c07dfc12f2dd5954af38'

    #url Api Call
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=current,minutely,hourly,daily,alerts&appid={api_key}'
   

    #response getter
    response = requests.get(url)
    

    # Check the HTTP status code
    if response.status_code == 200:
        #getting json data
        astronomical_data = response.json()

        #Accessing the data
        sunrise_phase = astronomical_data['current']['sunrise']
        sunset_phase = astronomical_data['current']['sunset']
        moon_phase = astronomical_data['current']['moon_phase']

        #Convert timestamps to human-readable format
        sunrise_time = datetime.utcfromtimestamp(sunrise_phase).strftime('%Y-%m-%d %H:%M:%S')
        sunset_time = datetime.utcfromtimestamp(sunset_phase).strftime('%Y-%m-%d %H:%M:%S')
        moon_str = "New Moon" if moon_phase == 0 else "Full Moon"
        
        #wrapper data for return 
        return_data = {'success': True,
                       'response': 'Success',
                       'sunrise_time':sunrise_time,
                       'sunset_time':sunset_time,
                       'moon_phase':moon_str


        }
        
        return return_data
    else:
        print(response.text)  # Print the response content for debugging
        return {'success': False, 'response': 'Something Went Wrong Please Try again !'}

#check code
check = currentAstronomyData(11.635250, 78.148880)
print(check)

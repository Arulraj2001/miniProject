import requests
import os

def currentWeatherData(latitude, longitude):
    api_key = '91e35b107a50bb5769307b4aaca1fef4'
    #url Api Call
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
   

    #response getter
    response = requests.get(url)
    

    # Check the HTTP status code
    if response.status_code == 200:
        #getting json data
        weather_data = response.json()


        #Accessing the data
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        rain = weather_data.get('rain', {}).get('1h', 'No Rainfall or Unable to detect at the specific location')  # 1-hour rainfall amount in mm
        snow = weather_data.get('snow', {}).get('1h', 'No Snowfall or Unable to detect at the specific location')  # 1-hour snowfall amount in mm
        atmospheric_pressure = weather_data['main']['pressure']
        cloud_coverage_percentage = weather_data['clouds']['all']
        uv_index = weather_data.get('uvi', 0)

        #wrapper data for return 
        return_data = {'success': True,
                       'response': 'Success',
                       'temperature':temperature,
                       'humidity':humidity,
                       'weather_description':weather_description,
                       'wind_speed':wind_speed,
                        'rain':rain,
                        'snow':snow,
                        'atmospheric_pressure':atmospheric_pressure,
                        'cloud_coverage_percentage':cloud_coverage_percentage,
                        'uv_index':uv_index

        }
        
        return return_data
    else:
        return {'success': False, 'response': 'Something Went Wrong Please Try again !'}



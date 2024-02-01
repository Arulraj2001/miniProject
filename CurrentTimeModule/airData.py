import requests
import os

def currentAirData(latitude, longitude):
    api_key = '91e35b107a50bb5769307b4aaca1fef4'

    #url Api Call
    url = f'https://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={api_key}'
   

    #response getter
    response = requests.get(url)
    

    # Check the HTTP status code
    if response.status_code == 200:
        #getting json data
        air_data = response.json()

        #Accessing the data
        air_quality_index = air_data['list'][0]['main']['aqi']
        air_quality_category = get_air_quality_category(air_quality_index)
        pm25 = air_data['list'][0]['components']['pm2_5']
        pm10 = air_data['list'][0]['components']['pm10']
        o3 = air_data['list'][0]['components']['o3']
        no2 = air_data['list'][0]['components']['no2']
        so2 = air_data['list'][0]['components']['so2']
        co = air_data['list'][0]['components']['co']

        #wrapper data for return 
        return_data = {'success': True,
                       'response': 'Success',
                       'air_quality_category':air_quality_category,
                       'pm25':pm25,
                       'pm10':pm10,
                       'o3':o3,
                       'no2':no2,
                       'so2':so2,
                       'co':co
                      

        }
        
        return return_data
    else:
        return {'success': False, 'response': 'Something Went Wrong Please Try again !'}
# air quality category
def get_air_quality_category(aqi):
    if aqi <= 50:
        return 'Good'
    elif aqi <= 100:
        return 'Moderate'
    elif aqi <= 150:
        return 'Unhealthy for Sensitive Groups'
    elif aqi <= 200:
        return 'Unhealthy'
    elif aqi <= 300:
        return 'Very Unhealthy'
    else:
        return 'Hazardous'

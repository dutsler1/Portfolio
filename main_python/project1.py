import requests
API_KEY = '3335bd0b656fa1498ebae689f300dddc'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    try:
        response = requests.get(BASE_URL, params={
            'q': city,
            'appid': API_KEY,
            'units': 'imperial'
        })
        response.raise_for_status()
        data = response.json()
        if "name" not in data or data['name'].lower() != city.lower():
            print(f'City "{city}" not found. Please check the name and try again.')
            return

        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        feels_like = data['main']['feels_like']

        print(f'Weather in {city.title()}:')
        print(f'Condition: {description}')
        print(f'Temperature: {temp}°F')
        print(f'Feels like: {feels_like}°F')
        print(f'Humidity: {humidity}%')

    except Exception as e:
        print(f'An error occured: {e}')

if __name__ == '__main__':
    city = input('Enter city name: ')
    get_weather(city)

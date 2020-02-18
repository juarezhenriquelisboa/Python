import requests
import json
import sys
from _datetime import datetime


def main():
    response = request_from_api()
    these_days = parse_response(response)
    print(f'You should take an umbrella in these days:', ', '.join(these_days), '.')


def request_from_api():
    api_key = 'YOUR_KEY'
    city_id = '3462284' #ID FROM GRAMADO/RS
    api_url = f'http://api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={api_key}'

    try:
        response = requests.get(api_url)
        return response.text
    except requests.exceptions.RequestException as error:
        print('Error: ', error)
        sys.exit(1)


def parse_response(response):
    result = json.loads(response)
    days_names = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    days_with_humidity = set([])
    days = set([])

    for info in result['list']:
        humidity = info['main']['humidity']

        if humidity > 70:
            day = datetime.strptime(info['dt_txt'], '%Y-%m-%d %X').weekday()
            days_with_humidity.add(day)

    for day in days_with_humidity:
        days.add(days_names[day])

    return days


if __name__ == '__main__':
    main()

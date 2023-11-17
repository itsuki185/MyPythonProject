import requests
import json

city_name = "Kobe" # 都市名として神戸しを指定。
API_KEY = "4710194fd6d56fd56a1ce5c364xxxxxx" # 取得したAPI Keyを入力。
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

url = api.format(city = city_name, key = API_KEY)
print(url)
response = requests.get(url)
data = response.json()
jsonText = json.dumps(data, indent=4)
print(jsonText)

    "base": "stations",
    "main": {
        "temp": 24.52,
        "feels_like": 24.72,
        "temp_min": 22.84,
        "temp_max": 25.82,
        "pressure": 1013,
        "humidity": 65
    },
    "visibility": 10000,
    "wind": {
        "speed": 3.09,
        "deg": 70
    },
    "clouds": {
        "all": 20
    },
    "dt": 1695941526,
    "sys": {
        "type": 1,
        "id": 7963,
        "country": "JP",
        "sunrise": 1695934302,
        "sunset": 1695977275
    },
    "timezone": 32400,
    "id": 1859171,
    "name": "Kobe",
    "cod": 200
}

プロセスは終了コード 0 で終了しました
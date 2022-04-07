import requests

s_city = "Moscow,RU"
appid = "2798864358e1ab04ede0c6fa87d4acc9"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

data = res.json()

# Погода в городе

print("*" * 10, "Погода в городе", "*" * 10)
print("Город: ", s_city)
print("Погодные условия: ", data['weather'][0]['description'])
print("Температура: ", data['main']['temp'])
print("Минимальная температура: ", data['main']['temp_min'])
print("Максимальная температура: ", data['main']['temp_max'])

# Прогноз погоды на неделю

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("*" * 10, "Прогноз погоды на неделю", "*" * 10)

for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
          "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
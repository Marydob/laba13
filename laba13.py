from tkinter import *
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Прогноз Погоды")

        self.cityField = Entry(root)
        self.cityField.pack()

        self.get_weather_button = Button(root, text="Получить прогноз погоды", command=self.get_weather)
        self.get_weather_button.pack()

        self.info = Label(root, justify=LEFT)
        self.info.pack()

    def get_weather(self):
        city = self.cityField.get()
        key = "60e7a39765d400d27f93b1cbf5a02f3e"
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': city, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()
        if 'main' in weather:
            temperature = weather['main']['temp']
            description = weather['weather'][0]['description']
            self.info.config(text=f'Город: {city}\nТемпература: {temperature}°C\nОписание: {description}')
        else:
            self.info.config(text="Город не найден")

        weekly_result = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=params)
        weekly_weather = weekly_result.json()
        weekly_forecast = 'Ежедневный прогноз:\n'
        for forecast in weekly_weather['list']:
            date = forecast['dt_txt']
            temperature = forecast['main']['temp']
            weekly_forecast += f'Дата: {date}, Температура: {temperature}°C\n'
        self.info.config(text=f'Город: {city}\nТемпература: {temperature}°C\nОписание: {description}\n\n{weekly_forecast}')
root = Tk()
app = WeatherApp(root)
root.mainloop()
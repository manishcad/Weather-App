from django.shortcuts import render
import requests
from django.contrib import messages
# Create your views here.


def home(request):
    hoax = False
    if request.method == "POST":
        try:
            city = request.POST.get("city")
            url = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1f336376d6aa73fb556789a977f5f6b4").json()

            des = url['weather'][0]['main']
            icon = url['weather'][0]['icon']
            temp = url['main']['temp']
            humidity = url['main']['humidity']
            wind_speed = url['wind']['speed']
            city_name = url['name']
            hoax = True
            print(des, icon, temp, humidity, wind_speed, city_name)
            context = {'des': des, 'icon': icon, 'temp': temp,
                       'humidity': humidity, 'wind': wind_speed, 'city': city_name, 'hoax': hoax}
            return render(request, 'home.html', context)
        except:
            messages.warning(request, "Enter A Valid City Addreess:")
            return render(request, 'home.html')

    return render(request, 'home.html')

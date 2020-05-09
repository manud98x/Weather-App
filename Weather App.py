import tkinter as tk
from tkinter import font
import requests

HEIGHT=500  
WIDTH=600



def format_jason(weather):

    try:

        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        tempmin = weather['main']['temp_min']
        tempmax = weather['main']['temp_max']
        humi = weather['main']['humidity']
        wind = weather['wind']['speed']
        pressure = weather['main']['pressure']
        sealevel = weather['main']['sea_level']

      
  
        



        f_str = 'City: %s \nConditions: %s \nTemperature(C): %s \nMin Temperature(C): %s\nMax Temparature(C): %s\nMax Humidity: %s\nWind Speed(km/h): %s\nPressure: %s\nSea Level: %s' % (name,desc,temp,tempmin,tempmax,humi,wind,pressure,sealevel)
    
    except:
        f_str = 'There was a problem retrieving information'

    return f_str 

def get_weather(city):
    
    weather_key = '5c2a009cc249e729e33422cd4fe6f67d'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params ={'APPID':weather_key,'q':city,'units':'Metric'}
    response = requests.get(url,params=params)
    weather = response.json()

    label['text'] = format_jason(weather)






root=tk.Tk()
root.title("Weather App")

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

bg_image = tk.PhotoImage(file="bg.png")
bg_label = tk.Label(root,image=bg_image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

frame = tk.Frame(root,bg="#3366ff",bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor="n")

entry = tk.Entry(frame,font="40")
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,text="Get Weather",bg="Grey",font="40",command= lambda:get_weather(entry.get()))
button.place(relwidth=0.3,relheight=1,relx=0.7)

lframe = tk.Frame(root,bg="#3366ff",bd=10)
lframe.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor="n")

label = tk.Label(lframe,font=('calibri'))
label.place(relwidth=1,relheight=1)

root.mainloop()



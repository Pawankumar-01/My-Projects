import tkinter as tk
from tkinter import *
import requests as r
import json
#linking and accessing the API
def get_weather():
    city=input.get()
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey=PyXzv9YQgSqBkcd4EI3Cu7eNnAroK68c"
    response = r.get(url)
    wdic=json.loads(response.text)
    temp=(wdic['data']['values']['temperature'])
    temp_label.config(text=f'Temperature in {city} is {temp}~C')

#creating widget
root=tk.Tk()
root.title("Weather")
root.geometry("500x500")
#creating input
input=tk.Entry(root,width=40)
input.pack()
#creating search button
button=tk.Button(root,text="Search",command=get_weather,width=10)
button.pack()
#creating temperature label
temp_label=tk.Label(root,text="",font='Ariel',width=30,height=20)
temp_label.pack()

root.mainloop()

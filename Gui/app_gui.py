import tkinter as tk
from tkinter import messagebox
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from WeatherCLI.weather import get_coordinates, get_weather
from cache import get_cached_data, cache_data

def ressource_path(path): 
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)


#Initializing a window object
window = tk.Tk()


##Functions
def update_search(city):

    try:
        #Getting the weather data
        cache = get_cached_data(city)
        if cache:
            weather = cache
        else:
        
            lat, lon = get_coordinates(city)
            weather = get_weather(lat,lon)
            cache_data(city, weather)

        cur_weather = weather["current_weather"]
        
        

        #Draw the window
        draw_ui(city, cur_weather)
        
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't get the weather.\n{e}")

def draw_ui(city, cur_weather ):
    wmo = {
        0:"Clear sky", 
        1:"Mainly clear", 2:"Partly cloudy",3:"Overcast",
        45:"Fog",48:"Depositing rime fog", 
        51:"Light drizzle", 53:"Moderate drizzle", 55:"Dense intensity drizzle",
        56:"Light freezing drizzle", 57:"Dense intensity freezing drizzle",
        61:"Slight rain", 63:"Moderate rain", 65:"Heavy intensity rain",
        66:"Light freezing rain", 67:"Heavy intensity freezing rain",
        71:"Slight snow fall", 73:"Moderate snow fall", 75:"Heavy intensity snow fall",
        77:"Snow grains",
        80:"Slight rain showers", 81:"Moderate rain showers", 82:"Violent rain showers",
        85:"Slight snow showers", 86:"Heavy snow showers", 
        95:"Thunderstorm",
        96:"Thunderstorm with slight hail", 99:"Thunderstorm with heavy hail"}
    code_to_pic = {
        0: "states/clear-sky.png",
        1: "states/clear-sky.png", 2:"states/clear-sky.png", 3:"states/overcast.png",
        45:"states/fog.png", 48:"states/fog.png",
        51: "states/drizzle.png", 53:"states/drizzle.png", 55:"states/drizzle.png",
        56: "states/freezingdrizzle.png", 57:"states/freezingdrizzle.png",
        61: "states/rainy.png", 63: "states/rainy.png", 65:"states/rainy.png",
        66:"states/freezing-rain.png", 67:"states/freezing-rain.png",
        71:"states/snow.png", 73:"states/snow.png", 75:"states/snow.png",
        77:"states/snow.png",  
        80:"states/rainy.png", 81:"states/rainy.png", 82:"states/rainy.png", 
        85:"states/snow.png", 86:"states/snow.png",
        95: "states/thunder.png",
        96: "states/thunder.png", 99: "states/thunder.png"}    
    
    canvas.delete("all")
    
    #The previous outline
    canvas.create_rectangle(20, 20, 340, 520, outline="#CEE9FA", width=6)

    #Rectangle to host the next elements
    canvas.create_rectangle(60, 170, 300, 480, fill="#CEE9FA", outline="#0094C6", width=6)
    
    #text/header
    canvas.create_text(180, 110, text="Weather at:", fill="#FBF9FF", font=("Helvetica", 18, "bold"))
    canvas.create_text(180, 150, text=f"{city.capitalize()}", fill="#FBF9FF", font=("Helvetica", 20, "bold"))
    
    #Show each photo assigned to a weather code
    canvas.state = tk.PhotoImage(file=ressource_path(code_to_pic[cur_weather["weathercode"]]))
    canvas.state = canvas.state.subsample(3, 3)
    canvas.create_image(175, 270, image=canvas.state)

    #line for aesthetics
    canvas.create_line(130, 370, 220, 370, fill="#0094C6", width=6)
    
    #Weather state
    canvas.create_text(175, 400, text=wmo[cur_weather["weathercode"]], font=("Helvetica", 18, "bold"), fill="#001242")

    #Thermometer picture
    canvas.thermo = tk.PhotoImage(file=ressource_path("images/thermometer.png"))
    canvas.thermo = canvas.thermo.subsample(16,16)

    canvas.create_image(120, 450, image=canvas.thermo)

    #Temperature
    string = f" :       {cur_weather["temperature"]}°C "
    canvas.create_text(190, 450, text=string, font=("Helvetica", 16, "bold"), fill="#001242")

def on_search():
    #Disable the button when pressed
    button.config(state="disabled")
    city = entry.get()
    update_search(city)
    #Enable it again 
    button.config(state="normal")

#Bind the enter key to the button
window.bind("<Return>", lambda event: on_search())



#name, size, background color of the window
window.title("WeatherApi")
window.geometry("360x540")
window.config(background="#000022")
window.resizable(False, False)

#window icon
icon = tk.PhotoImage(file=ressource_path("images/weather_icon.png"))
window.iconbitmap()

#exe icon
icon_path = ressource_path("images/icon.ico")
window.iconbitmap(icon_path)

#canvas that will host everything
canvas = tk.Canvas(window, bg = "#001242", border=None)
canvas.pack(fill=tk.BOTH, expand=True)

#Rectangle/ padded outline
canvas.create_rectangle(20, 20, 340, 520, outline="#CEE9FA", width=6)

#Entry widget
entry = tk.Entry(window, font=("Helvetica", 18), justify="center", background="#CEE9FA")
entry.place(x=55, y=50, width=250, height=30)

#Search Button
search = tk.PhotoImage(file=ressource_path("images/search.png"))
search = search.subsample(20,20)

button = tk.Button(window, image=search, command=on_search)
button.place(x=280, y=50)

#Underlined text
canvas.create_text(180, 170, text="Weather App", font=("Helvetica", 34, "bold"), anchor="center", fill="#FBF9FF")

canvas.create_line(50, 210, 310, 210, width=6, fill="#CEE9FA")

#Image in the center of it
photo = tk.PhotoImage(file=ressource_path("images/cloudy.png"))
photo = photo.subsample(2,2)

image1 = canvas.create_image(180, 350, image=photo, anchor="center")


#open the window
window.mainloop()


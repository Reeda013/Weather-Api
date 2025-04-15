#!/usr/bin/env python

import requests 
import argparse

def get_weather(lat, lon):
    #Connect to the weather api
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    #send the request
    response = requests.get(url=url, params=params)

    if not response.ok:
        raise RuntimeError("Unable to fetch data!")

    return response.json()

    
def get_coordinates(city):
    
    #Connect into a geocode api
    url = "https://geocoding-api.open-meteo.com/v1/search?"
    params = {
        "name": city,
        "count": 1  #count is 1 to limit the search
    }
    
    #send the request
    response = requests.get(url=url, params=params)

    if not response.ok:
        raise RuntimeError("Failed to fetch coordinates!")

    data = response.json()

    if "results" not in data or not data["results"]:
        raise argparse.ArgumentTypeError("Invalid city name!")
        
    #Extract the latitude and longitude
    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]
    return (lat, lon)
    
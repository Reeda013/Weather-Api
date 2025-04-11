import argparse
import json
from WeatherCLI.weather import get_coordinates, get_weather

def valid_city(city):

    if not city.isalpha():
        raise argparse.ArgumentTypeError("Invalid city name!")
    else:
        return city
    

def main():
    
    #Handling the arguments
    
    parser = argparse.ArgumentParser(description="Check the weather anywhere from the command line!")
    parser.add_argument("city", type=valid_city)
    parser.add_argument("--save", "-s", required=False, action="store_true", help="Save the weather data into a file!")
    
    args = parser.parse_args()
    
    #Getting the coordinates
    print("Fetching coordinates...", flush=True)
    lat, lon = get_coordinates(args.city)

    #Getting the weather data
    print("Fetching weather data...\n", flush=True)
    weather = get_weather(lat, lon)
    
    if args.save:
        with open(f"{args.city}.json", "w") as file:
            json.dump(weather, file, indent=4)
            print("Successfully saved the data!")
    else:
        
        #Each weather is assigned to a code, this dictionary serves as a way
        #to get the weather type from the code
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
        96:"Thunderstorm with slight hail", 99:"Thunderstorm with heavy hail" 
    }
        print(f"The weather is: {wmo.get(weather["current_weather"]["weathercode"], "Unknown weather.")}")
        print(f"It is {weather["current_weather"]["temperature"]} degrees!")

if __name__ == "__main__":
    main()
# Weather App
---
# Cli version 
A simple CLI tool to check the weather anywhere from the comfort of your terminal.
solution for https://roadmap.sh/projects/weather-api-wrapper-service

## Installation
To install the package:
```bash
pip install git+https://github.com/Reeda013/weather-cli.git
```
## Usage
```bash
#To check the weather
weather-cli <city-name>

#To save said weather data into a file
weather-cli <city-name> --save
```
---
# Gui version
This one is a Gui version that can be turned into a.exe

![Screenshot 2025-04-15 234220](https://github.com/user-attachments/assets/e2078a29-bc32-49d4-8e91-c66ff2f661ff)                         ![image](https://github.com/user-attachments/assets/112cbc35-45de-4ef9-8d77-b804103534bb)

## To install as .exe
```bash
#Install pyinstaller
pip install pyinstaller

#Run
pyinstaller --noconsole --onefile --add-data "Gui/images;images" --add-data "Gui/states;states"

#The .exe will be in the dist folder

```




## License
Licensed by MIT

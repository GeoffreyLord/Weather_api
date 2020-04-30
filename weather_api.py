#Python 3
#Created By: Geoffrey G. Lord, Jr.
#Date: April 27 2020
#Weather API

import requests
import json
import time
#Link Below was able to provide list of other API's. One was weather
#User Input
lat = input("Enter latitude (dec): ")
long = input("Enter longitude (dec): ")
url = "https://api.weather.gov/points/" + lat + "," + long

#API Request and Parsing for Grid Points
grid = (requests.get(url)).text
grid_index = (grid.index("/forecast"))
x = grid[grid_index - 2] + grid[grid_index - 1]
y = grid[grid_index - 5] + grid[grid_index - 4]


#This Request will get the hourly weather data in JSON format 
weather = requests.get("https://api.weather.gov/gridpoints/BOU/" + x + ',' + y + "/forecast/hourly")
weather = weather.text

#Parse Data
#Get indecies from current hour 
start_ind = weather.index('"number": 1,')
end_ind = weather.index('"icon": "https://api.weather.gov/icons/land/night/skc?size=small",')


current_weather = [None]*((end_ind-start_ind)+4)
for i in range(start_ind,end_ind+4):
	current_weather[i-start_ind] = weather[i]
current_weather = ''.join(current_weather)

#Parsing Current Weather Into Clean Output
temp_index = current_weather.index('ture":')
temp = current_weather[temp_index + 7] + current_weather[temp_index + 8]
windspeed_ind = current_weather.index('Speed": "')
wind_speed = current_weather[windspeed_ind + 9] + ' mph'
winddirect_ind = current_weather.index('Direction": "')
wind_direction = current_weather[winddirect_ind + 13] + current_weather[winddirect_ind + 14] + current_weather[winddirect_ind + 15]

#Get Local Time
localtime = time.asctime( time.localtime(time.time()) )
#Print Weather at Current Time/Location
print('\n'*3)
print('\tCURRENT WEATHER\t -- LAT: ' + lat +  ", LONG: " + long)
print(' ')
print("\tTime: " +  localtime)
print("\tTemperature: " + temp + "F")
print("\tWind Speed: " + wind_speed) 
print("\tWind Direction: " + wind_direction)
print('\n')




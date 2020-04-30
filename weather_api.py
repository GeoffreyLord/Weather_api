#Python 3
#Created By: Geoffrey G. Lord, Jr.
#Date: April 27 2020
#Weather API

import requests
import json

#Link Below was able to provide list of other API's. One was weather
#weather = requests.get("https://api.weather.gov/points/39.7348,-104.9653")

#This Request will get the weather data in JSON format 
#To get gridpoints enter in your coords to this api
#https://api.weather.gov/points/{latitude},{longitude}

#20 20
#44 56
weather = requests.get("https://api.weather.gov/gridpoints/BOU/44,56/forecast")

#Want data from lines 66-77 
weather = weather.text
#weather = json.loads(weather)
print(weather)
#Parse Data 
start_ind = weather.index("name")
end_ind = weather.index("mph.")
#print(start_ind,end_ind)

current_weather = [None]*((end_ind-start_ind)+4)
for i in range(start_ind,end_ind+4):
	current_weather[i-start_ind] = weather[i]
current_weather = ''.join(current_weather)
print('\n'*3)
print(current_weather)
print('\n'*3)

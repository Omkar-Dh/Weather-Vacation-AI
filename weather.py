import requests
import json
import chat

class Requests:
    
    def getWeather(self,lat,long):

        coordinateUrl = f"https://api.weather.gov/points/{lat},{long}"
        
        coordinateJson = requests.get(coordinateUrl)

        gridUrl = coordinateJson.json()['properties']['forecast']

        gridJson = requests.get(gridUrl)


        dayForecast = []
        nightForecast = []
        forecastDays = len(gridJson.json()['properties']['periods'])

        for x in range(0, forecastDays):
            if(x % 2 == 0):
                dayForecast.append(gridJson.json()['properties']['periods'][x])
            else:
                nightForecast.append(gridJson.json()['properties']['periods'][x])
        

        return dayForecast, nightForecast
    
    def locationFinder(self, lat, long, previousLocations, weatherData):
        detailedForecast = weatherData['detailedForecast']

        timeOfDay = 'day time' if (weatherData['isDaytime']) else 'night time'

        prompt = (f"Given that it is {timeOfDay}, and the weather is {detailedForecast}"
          f" What is a specific location to visit near the latitude and longitude coordinates, {lat}, {long}."
          f"Give me a location I have not visited, I have already visited these locations: {', '.join(previousLocations)}."
          "List the location name with no other infomation like the city name.")

        c = chat.Chat(prompt,1024)

        return(c.getResponse())
        

        




        

        






        

        
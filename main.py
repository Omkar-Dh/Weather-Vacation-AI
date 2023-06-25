import chat
import weather

prompt = input("Enter Location: ")
days = int(input("Enter Vacation Length (Today is Day 1):"))
botEmoji = u"\U0001F916"
print(f"{botEmoji} Finding locations...")

c = chat.Chat(prompt,1024)
c.coordinateFormatting()


response = c.getResponse()
latitude = float(response.split(",")[0].strip())
longitude = float(response.split(",")[1].strip())

w = weather.Requests()

dayForecast, nightForecast = w.getWeather(latitude,longitude)

dayplan = []
nightplan = []

for i in range(days):
    combinedLists = dayplan+nightplan
    dayplan.append(w.locationFinder(latitude, longitude, combinedLists, dayForecast[i]).strip())
    nightplan.append(w.locationFinder(latitude, longitude, combinedLists, nightForecast[i]).strip())

for i in range(1, days+1):
    print("Day " + str(i) + ": ")
    print(dayplan[i-1])
    print("\nNight " + str(i) + ": ")
    print(nightplan[i-1])
    print("\n")
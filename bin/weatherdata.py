import json, requests, time, datetime

# config od openweather map api / key / city id
key = 'YOUR KEY HERE'
units = 'metric'
cityid = '650224'
sleep_time = 3600 #seconds between calls (data is updated every 2 hours)

def SaveData( filename, data ):
	# save location
	saveloc = "/home/weather/data/"
 	"save data with filename int path /home/weather/data"
	f = open('{}{}'.format(saveloc,filename),'w+')
 	f.write(data)
 	f.close()
 	return;

url=requests.get('http://api.openweathermap.org/data/2.5/weather?id='+cityid+'&units='+units+'&APPID='+key)

while True:
 weather = json.loads(url.text)
 SaveData( filename='timestamp.log', data=str(weather['dt']))
 SaveData( filename='outdoor.log', data=str(weather['main']['temp']))
 SaveData( filename='weather_id.log', data=str(weather['weather'][0]['id']))
 SaveData( filename='wind.log', data=str(weather['wind']['speed']))
 SaveData( filename='humidity.log', data=str(weather['main']['humidity']))

 time.sleep(sleep_time); # delay  (api weather data is update every 2 hours on servers)
 # weather condition codes -> https://openweathermap.org/weather-conditions

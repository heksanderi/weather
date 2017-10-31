import json, requests, time, datetime

# config od openweather map api / key / city id
key = 'YOUR API KEY'
units = 'metric'
cityid = '650224'
sleep_time = 3600 #seconds between calls (data is updated every 2 hours)
def myprint(d, root,index):
  rootfolder = "{}.".format(root)
  if not root:
   rootfolder = ""
  for k, v in d.items():
    if isinstance(v, dict):
      myprint(v,"{}{}".format(rootfolder,k),index)
    elif isinstance(v, list):
	for ke in v:
         index += 1
         myprint(ke,"{}{}".format(rootfolder,k),index)
    else: 
      #print("{0}{1} : {2}".format(rootfolder,k, v))
      SaveData("{}{}_{}".format(rootfolder,k,index),"{}".format(v))

def SaveData( filename, data ):
	""" SaveData(
		filename - name of file to be saved
		data - data string to be saved
		)
		Function will overwrite whole file.
		File is created if it does not exist
	"""
	saveloc = "../data/"
	f = open('{}{}'.format(saveloc,filename),'w+')
 	f.write(data)
 	f.close()
 	return;

urlf=requests.get('http://api.openweathermap.org/data/2.5/forecast?id='+cityid+'&units='+units+'&APPID='+key)
urlw=requests.get('http://api.openweathermap.org/data/2.5/weather?id='+cityid+'&units='+units+'&APPID='+key)

while True:
 weather = json.loads(urlw.text)
 #print weather
 forecast = json.loads(urlf.text)
 #print forecast
 myprint(weather,"weather",0)
 myprint(forecast,"forecast",0)
 #print "{}".format(type(weather['weather'])) 
 #quit()
 time.sleep(sleep_time); # delay  (api weather data is update every 2 hours on servers)
 # weather condition codes -> https://openweathermap.org/weather-conditions

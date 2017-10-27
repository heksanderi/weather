# weather-pi
Script for reading weather data and forecast from open weather map into filesystem on rasperry pi (for talologger / OWFS)

<h2>Installation and configuration</h2>

By default the script assumes it is installed in /home/weather/ 
If you want to change this you must edit the following files:
<ul>
  <li>/bin/weatherdata.py</li>
  <li>/bin/runweather.sh</li>
  <li>use your actual location in rc.local startup script</li>
  </ul>

Clone the project and give permimssions:
<pre>
sudo git clone https://github.com/heksanderi/weather.git /home/weather
sudo chown root /home/weather/bin/runweather.sh
sudo chmod u+x /home/weather/bin/runweather.sh
</pre>
<h2>Configuration</h2>
<ul>
  <li>Get api key from openweathermap: http://openweathermap.org/appid
  <li>Get location id for your city/area http://openweathermap.org/find and get the numer code from url: http://openweathermap.org/city/7645026 has city/location id of 7645026
  </ul>


Set variables in weather/bin/weatherdata.py
<pre>
 key = 'YOUR API KEY HERE'
 units = 'metric'
 cityid = '650224'
</pre>

<h2>Test the script</h2>
<pre>
  sudo python /home/weather/bin/weatherdata.py
</pre>
Press CTRL+C to terminate script after a few seconds
Check that the timestamps of your data files are updated
<pre>
ls -l /home/weather/data/
</pre>

The script is configured to read weather data once per hour by default (sleep_time = 3600)

You can set the script to run on startup by editing rc.local
<pre>
  sudo pico /etc/rc.local
</pre>

Add the following and exit with CTRL+X and saving changes with 'y'
<pre>
/home/weather/bin/runweather.sh &
</pre>

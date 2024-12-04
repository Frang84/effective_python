from datetime import datetime, timedelta
import pytz 
from countryinfo import countries
import time

def printCurrTime():
    sortedCountries = sorted(countries, key=lambda x: x['continent'])
    currContinent = ''

    for country in sortedCountries: 
        if currContinent != country['continent']: 
            currContinent = country['continent']
            print(f'=========={currContinent}==========')
        currTz = pytz.timezone(country['timezones'][0])
        currTime = datetime.now(currTz)
        print(f'current time in {country['timezones'][0]} is {currTime.strftime("%H:%M:%S")}')



def get_seconds_to_midnight(timezone):
    """Oblicz liczbę sekund do najbliższej północy w podanej strefie czasowej."""
    now = datetime.now(pytz.timezone(timezone))
    midnight = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    return (midnight - now).total_seconds()



country_times = []
for country in countries:
    for timezone in country['timezones']:
        seconds_to_midnight = get_seconds_to_midnight(timezone)
        country_times.append((seconds_to_midnight, country['name'], timezone))


country_times.sort()


print("Symulacja wybicia północy w różnych krajach:")
for seconds, country_name, timezone in country_times:
    print(f"Następne wybicie północy: {country_name} (Strefa: {timezone})")
    time.sleep(seconds / 10)  






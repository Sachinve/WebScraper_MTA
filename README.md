# Web Scraper to collect realtime location of MTA Buses

### Requirements
* To use this web scraper you would need to register at the MTA website and get the API key to access the data

## show_bus_locations.py
* This python script (show_bus_locations.py) would show the location of the New York MTA Bus Route supplied as argument.
* Its usage is as follows:
   * python show_bus_locations.py \<MTA_API_KEY\> \<BUS_ROUTE\>


## get_bus_info.py 
* This python script (get_bus_info.py) would dump the current latitude,longitude,stopname and stopstatus for New York MTA Bus Route supplied as argument. It's output would be a csv file supplied as 3rd argument to script
* Its usage is as follows:
   * python get_bus_info.py \<MTA_API_KEY\> B52 B52.csv
   * above command would fetch you the location of all the buses running on route B52 in NYC

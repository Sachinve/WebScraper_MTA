#!/usr/bin/env python
#
#   Author: Sachin Verma                                #
#   Email: sv1379@nyu.edu                               #
#########################################################

import json
import sys
import urllib2
import csv

def prog_help():
    print 'Sample Usage:'
    print 'python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx B52 B52.csv'

if __name__=='__main__':
    baseurl = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={0}&VehicleMonitoringDetailLevel=calls&LineRef={1}'

    if len(sys.argv) < 4:
        print 'Not enough arguments'
        prog_help()
        sys.exit()

    userkey = sys.argv[1]
    busline = (sys.argv[2]).upper()

    url = baseurl.format(userkey,busline)
try:
    request = urllib2.urlopen(url)
except urllib2.HTTPError, e:
    print 'HTTPError = ' + str(e.code)
except urllib2.URLError, e:
    print 'URLError = ' + str(e.reason)
except httplib.HTTPException, e:
    print 'HTTPException'
except Exception:
    import traceback
    print 'generic exception: ' + traceback.format_exc()
else:
    data = json.loads(request.read())
    busroute_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]

    if 'VehicleActivity' not in busroute_data:
        print 'Error--->  {0} : No such route exists'.format(busline)
        sys.exit()

    buslist = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    if len(buslist) == 0:
        print '{0} : No Buses are Active currently on this Route'.format(busline)
        sys.exit()
    else:
        print 'Bus Line: ' + busline
        print 'Number of Active Buses : {0}'.format(len(buslist))

    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)
        for b in buslist:
            vehicle_location = b['MonitoredVehicleJourney']['VehicleLocation']
            VehicleRef = b['MonitoredVehicleJourney']['VehicleRef']
            onward_calls = b['MonitoredVehicleJourney']['OnwardCalls']
            if 'OnwardCall' not in onward_calls:
                stop = 'N/A'
                status = 'N/A'
            else:
                status = onward_calls['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
                stop = onward_calls['OnwardCall'][0]['StopPointName']
            writer.writerow([vehicle_location['Latitude'], vehicle_location['Longitude'],stop, status])



import ephem
from astropy.coordinates import EarthLocation
from astropy.coordinates import Angle
from astropy.time import Time
from astropy import units as u
import datetime
from pytz import timezone
from astropy import coordinates as coord
 

my_zone = timezone('Asia/Kolkata')
sa_time = datetime.datetime.now(my_zone)

my_curr_time = sa_time.strftime('%Y-%m-%d %H:%M:%S')
print("Current time for your location : ",my_curr_time)

observing_location = EarthLocation(lat = 31.7754*u.deg, lon = 76.9861*u.deg)
observing_time = Time(datetime.datetime.now(), scale='utc', location=observing_location)

print("Current UTC time : ",observing_time)

LST = observing_time.sidereal_time('mean')
a = Angle(LST, u.radian)
print("Local Sideral Time : ",LST)
#print(a.degree,"\n")

target = ephem.star('Polaris')
#m = '%s' % (target._ra)
RA = target._ra
b = Angle(RA, u.radian)
#print(b.degree,"\n")
print("RA of Polaris : ",RA)

hour_angle = a.degree-b.degree

#print('hour_angle in degree is:',hour_angle)

if hour_angle >= 0:
  hour_angle = hour_angle
else:
  hour_angle = 360.00 + hour_angle
  
c = Angle(hour_angle, u.degree)
#print(c.degree,"\n")

print('The required hour angle : ',c.to_string(unit=u.hour))


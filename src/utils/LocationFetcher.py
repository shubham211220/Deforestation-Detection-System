# Import the required library
from geopy.geocoders import Nominatim


def getLocationMsg(percentage):
        
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="MyApp")
    
    location = geolocator.geocode("Sangamner")
    
    print("The latitude of the location is: ", location.latitude)
    print("The longitude of the location is: ", location.longitude)
    lat=str(location.latitude)
    longi=str(location.longitude)
    
    urlstr="https://www.google.com/maps/dir/"+lat+","+longi
    strper=str(percentage)
    message="Deforestation is happening with"+ strper+ " %  at this location : "+urlstr
    return message
  

#print(urlstr)
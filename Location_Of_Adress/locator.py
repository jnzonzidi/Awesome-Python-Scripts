import geocoder

# Prompt the user for the location
location = input("Enter the location: ").strip()

# Get the latitude and longitude using ArcGIS
g = geocoder.arcgis(location)

# Check if the location was successfully geocoded
if g.latlng:
    print(f"The latitude and longitude of '{location}' are: {g.latlng}")
else:
    print(f"Could not retrieve coordinates for the location: {location}")



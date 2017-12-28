
# coding: utf-8

# # WeatherPy
Your objective is to build a series of scatter plots to showcase the following relationships:

* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude

Your final notebook must:

* Randomly select **at least** 500 unique (non-repeat) cities based on latitude and longitude.
* Perform a weather check on each of the cities using a series of successive API calls. 
* Include a print log of each city as it's being processed with the city number, city name, and requested URL.
* Save both a CSV of all data retrieved and png images for each scatter plot.

As final considerations:

* You must use the Matplotlib and Seaborn libraries.
* You must include a written description of three observable trends based on the data. 
* You must use proper labeling of your plots, including aspects like: Plot Titles (with date of analysis) and Axes Labels.
* You must include an exported markdown version of your Notebook called  `README.md` in your GitHub repository.  
* See [Example Solution](WeatherPy_Example.pdf) for a reference on expected format. 
# In[84]:


#Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn
import requests as req
from citipy import citipy
from random import *


# In[85]:


#COULD NOT FIGURE OUT HOW TO CREATE RANDOM COORDINATES THAT DO NOT REPEAT
#Managed to create random coordinates however.

#Create a blank list where random coordinates would append to
coord_list = []

#Create function that creates x,y coordinates based on actual coordinate min and max
def rand_coord():
    return uniform(-90,90), uniform(-180, 180)

#Run function x times
coordinates = (rand_coord() for x in range(400)) #of total pairs

#Create for loop that grabs 
for point in coordinates:
    coord_list.append(point)

#Check results are coorect
print(coord_list)


# In[87]:


cities = []
city_list = []
row_count = 0

for coordinate_pair in coord_list:
    lat, lon = coordinate_pair
    cities.append(citipy.nearest_city(lat, lon))

for city in cities:
    name = city.city_name.title()
    row_count += 1
    city_list.append(name)
    if row_count < 401: #maximum number of repetition. Should be changed to 500
        print("Random city #", row_count, name)
    else:
        continue


# In[88]:


city_df = pd.DataFrame(city_list)

city_df["latitude"]=""
city_df["temperature"]=""
city_df["humidity"]=""
city_df["cloudiness"]=""
city_df["wind_speed"]=""
city_df = city_df.rename(columns={0:"city_name"})

city_df.tail()


# In[89]:


cities = []

for index, row in city_df.iterrows():
    cities = row["city_name"]
    query_url=  "http://api.openweathermap.org/data/2.5/weather?units=imperial&q=%s&appid=%s" % (cities.replace(" ","+"), api_key)
    weather = req.get(query_url).json()
    
    try:
        city_df.set_value(index, "latitude", weather["coord"]["lat"])
        city_df.set_value(index, "temperature", weather["main"]["temp"])
        city_df.set_value(index, "humidity", weather["main"]["humidity"])
        city_df.set_value(index, "cloudiness", weather["clouds"]["all"])
        city_df.set_value(index, "wind_speed", weather["wind"]["speed"])
        print("- ", end="")
                   
    except:
        continue
        
city_df


# In[100]:


city_df['latitude'].replace('', np.nan, inplace=True)
city_df.dropna(subset=["city_name"], inplace=True)
city_df.dropna(subset=["latitude"], inplace=True)
city_df


# In[102]:


plt.scatter(city_df.latitude, city_df.temperature, marker="o", facecolors="red", edgecolors="black")

plt.title("City Latitude vs. Temperature")
plt.xlabel("Latitude")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()


# In[103]:


plt.scatter(city_df.latitude, city_df.humidity, marker="o", facecolors="red", edgecolors="black")

plt.title("City Latitude vs. Humidity")
plt.xlabel("Latitude")
plt.ylabel("Humidity")
plt.grid(True)
plt.show()


# In[104]:


plt.scatter(city_df.latitude, city_df.cloudiness, marker="o", facecolors="red", edgecolors="black")

plt.title("City Latitude vs. Cloudiness")
plt.xlabel("Latitude")
plt.ylabel("Cloudiness")
plt.grid(True)
plt.show()


# In[105]:


plt.scatter(city_df.latitude, city_df.cloudiness, marker="o", facecolors="red", edgecolors="black")

plt.title("City Latitude vs. Wind Speed")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed")
plt.grid(True)
plt.show()


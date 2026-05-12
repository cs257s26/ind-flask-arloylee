# README

Configure the port with the variable PORT in app.py

## Flask Usage & Examples

- To see water data for all years for a given location, enter http://127.0.0.1:PORT/search/loc/LOCATION  
For example: `http://127.0.0.1:PORT/search/loc/Afghanistan`

- To see water data for all locations for a given year, enter http://127.0.0.1:PORT/search/year/YEAR  
For example: `http://127.0.0.1:PORT/search/year/2005`

- To see water data for a specific location and year, enter http://127.0.0.1:PORT/LOCATION/YEAR  
For example: `http://127.0.0.1:PORT/Afghanistan/2005`

## PSQL commands

\copy water_country FROM 'Data/Water_Country.csv' DELIMITER ',' CSV HEADER
\copy water_region FROM 'Data/Water_Region.csv' DELIMITER ',' CSV HEADER

## Database Write-Up

I chose the data for this database by focusing on the accessibility of water by country and region. The original data had subdivisions by rural vs urban settings, but I consolidated it to just local information. I eliminated some irrelevant data points, like surface water or rate of change for specific variables, which I felt would not serve my user stories. I wanted to focus on the availability of water and its quality. My primary keys are location and year.

I have two queries, one that gets the data for a specific location and year, and one that gets the data for all years for a location. These apply to the user stories my team compiled in our group project repo, for example, a traveller who wants to know more about a specific location at this current time, specifically, or a researcher who wants to know how the availability of water has changed in a location over time.
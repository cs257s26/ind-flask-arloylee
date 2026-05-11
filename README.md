# README

Configure the port with the variable PORT in app.py

## Usage & Examples

- To see water data for all years for a given location, enter http://127.0.0.1:PORT/search/loc/LOCATION  
For example: `http://127.0.0.1:PORT/search/loc/Afghanistan`

- To see water data for all locations for a given year, enter http://127.0.0.1:PORT/search/year/YEAR  
For example: `http://127.0.0.1:PORT/search/year/2005`

- To see water data for a specific location and year, enter http://127.0.0.1:PORT/LOCATION/YEAR  
For example: `http://127.0.0.1:PORT/Afghanistan/2005`

## PSQL commands

\copy water_country FROM 'Data/Water_Country.csv' DELIMITER ',' CSV HEADER
\copy water_region FROM 'Data/Water_Region.csv' DELIMITER ',' CSV HEADER
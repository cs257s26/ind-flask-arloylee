"""datasource.py

Code to fetch querys from water data
"""

import psycopg2 as ps
import psqlConfig as config

def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

def get_water_data_year_and_location(connection, location: str, year: int) -> list:
    """Retrieves the data associated with a particular year and location

    Args:
        connection (psycopg2.connection) - the connection to the database
        location (str) - the requested string
        year (int) - the requested year

    Returns:
        list - a list of all data that matches both the year and location
    """
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM water_country WHERE country = %s AND year = %s UNION ALL SELECT * FROM water_region WHERE region = %s AND year = %s;"
        cursor.execute(query, (location, year, location, year))
        return cursor.fetchall()
    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def get_water_data_location(connection, location: str) -> list:
    """Retrieves the data associated with a particular location

    Args:
        connection (psycopg2.connection) - the connection to the database
        location (str) - the requested string

    Returns:
        list - a list of all data that matches the location
    """
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM water_country WHERE country = %s UNION ALL SELECT * FROM water_region WHERE region = %s;"
        cursor.execute(query, (location, location,))
        return cursor.fetchall()
    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_water_data_year_and_location(connection, "Afghanistan", 2005)
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)
            
    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_water_data_location(connection, "Oceania")
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

main()

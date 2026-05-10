DROP TABLE IF EXISTS water_Region;
CREATE TABLE water_Region (
  weather_date DATE,
  max_temp REAL,
  min_temp REAL,
  precip TEXT,
  snow TEXT,
  snow_depth TEXT
);

DROP TABLE IF EXISTS water_Country;
CREATE TABLE water_Country (
  weather_date DATE,
  max_temp REAL,
  min_temp REAL,
  precip TEXT,
  snow TEXT,
  snow_depth TEXT
);
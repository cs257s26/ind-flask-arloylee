DROP TABLE IF EXISTS weather_small;
CREATE TABLE weather_small (
  weather_date DATE,
  max_temp REAL,
  min_temp REAL,
  precip TEXT,
  snow TEXT,
  snow_depth TEXT
);
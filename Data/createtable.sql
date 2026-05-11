DROP TABLE IF EXISTS water_country;
CREATE TABLE water_country (
  country TEXT,
  year REAL,
  population_thou TEXT,
  urban_perc REAL,
  basic_perc REAL,
  limited_prec REAL,
  unimproved REAL,
  safely_managed REAL,
  accessible REAL,
  available REAL,
  no_contamination REAL,
  piped REAL,
  non_piped REAL
);

DROP TABLE IF EXISTS water_region;
CREATE TABLE water_region (
  region TEXT,
  year REAL,
  population_thou REAL,
  urban_perc REAL,
  basic_perc REAL,
  limited_prec REAL,
  unimproved REAL,
  safely_managed REAL,
  accessible REAL,
  available REAL,
  no_contamination REAL,
  piped REAL,
  non_piped REAL
);
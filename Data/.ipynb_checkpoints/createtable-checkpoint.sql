DROP TABLE IF EXISTS water_country;
CREATE TABLE water_country (
  country TEXT,
  year REAL,
  population_thou TEXT,
  urban_perc TEXT,
  basic_perc TEXT,
  limited_prec TEXT,
  unimproved TEXT,
  safely_managed TEXT,
  accessible TEXT,
  available TEXT,
  no_contamination TEXT,
  piped TEXT,
  non_piped TEXT
);

DROP TABLE IF EXISTS water_region;
CREATE TABLE water_region (
  region TEXT,
  year REAL,
  population_thou TEXT,
  urban_perc TEXT,
  basic_perc TEXT,
  limited_prec TEXT,
  unimproved TEXT,
  safely_managed TEXT,
  accessible TEXT,
  available TEXT,
  no_contamination TEXT,
  piped TEXT,
  non_piped TEXT
);

DROP TABLE IF EXISTS emissions CASCADE;
DROP TABLE IF EXISTS meters CASCADE;
DROP TABLE IF EXISTS metrics;
DROP TABLE IF EXISTS fuelOil;

CREATE TABLE emissions (
    units char(50) UNIQUE NOT NULL,	
    meter_type char(30) NOT NULL,
    avg_emissions float NOT NULL,
    PRIMARY KEY (units)
);

CREATE TABLE meters (
	meter_name char(30) UNIQUE NOT NULL,
	meter_type char(20) NOT NULL,
	units char(50) NOT NULL,
    PRIMARY KEY (meter_name)
);

CREATE TABLE metrics (
	meter_name char(30) NOT NULL,
	consumption_id char(50) UNIQUE NOT NULL,
	start_date DATE NOT NULL,
    usage_quantity float(10) NOT NULL,
	cost decimal(8,2) NOT NULL,
    PRIMARY KEY (consumption_id)
);


CREATE TABLE fuelOil (
	meter_name char(30) NOT NULL,
    consumption_id char(50) UNIQUE NOT NULL,
    usage_quantity float NOT NULL,
	cost decimal(8,2) NOT NULL,
    delivery_day DATE NOT NULL,
    PRIMARY KEY (consumption_id)
);

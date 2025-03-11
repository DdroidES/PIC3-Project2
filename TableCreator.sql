CREATE TABLE Humidity (
    id SERIAL PRIMARY KEY
    timestamp VARCHAR(255) ,
    value FLOAT
);

CREATE TABLE Irrigation (
    id SERIAL PRIMARY KEY ,
    timestamp VARCHAR(255) ,
    value  FLOAT
);

CREATE TABLE RainGauge (
    id SERIAL PRIMARY KEY ,
    timestamp VARCHAR(255) ,
    value  FLOAT
);

CREATE TABLE Temperature (
    id SERIAL PRIMARY KEY ,
    timestamp VARCHAR(255) ,
    value  FLOAT
);
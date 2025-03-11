CREATE TABLE Humidity ( ,
    timestamp VARCHAR(255) PRIMARY KEY,
    value FLOAT
);

CREATE TABLE Irrigation (
    id SERIAL PRIMARY KEY ,
    timestamp VARCHAR(255) REFERENCES Humidity(timestamp),
    value  FLOAT
);

CREATE TABLE RainGauge (
    id SERIAL PRIMARY KEY ,
    timestamp VARCHAR(255) REFERENCES Humidity(timestamp),
    value  FLOAT
);

CREATE TABLE Temperature (
    id SERIAL PRIMARY KEY ,
    timestamp VARCHAR(255) REFERENCES Humidity(timestamp),
    value  FLOAT
);
-- Production Line Table
CREATE TABLE Production_Line (
    line_id INT PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    curr_state BOOL NOT NULL
);

-- Production Line State Table
CREATE TABLE production_line_state (
    state BOOLEAN PRIMARY KEY
);

-- Production Line State History Table
CREATE TABLE production_line_state_history (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    state BOOLEAN NOT NULL,
    FOREIGN KEY (state) REFERENCES production_line_state(state),
    line_id INT NOT NULL,
    FOREIGN KEY (line_id) REFERENCES Production_Line(line_id)
);

-- Station Table
CREATE TABLE Station (
    station_id INT PRIMARY KEY,
    type VARCHAR(50) NOT NULL, 
    prod_line INT NOT NULL,
    FOREIGN KEY (prod_line) REFERENCES Production_Line(line_id),
    curr_state BOOL NOT NULL
);

-- Station State Table
CREATE TABLE station_state (
    state BOOLEAN PRIMARY KEY
);

-- Station State History Table
CREATE TABLE station_state_history (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    state BOOLEAN NOT NULL,
    FOREIGN KEY (state) REFERENCES station_state(state),
    station_id INT NOT NULL,
    FOREIGN KEY (station_id) REFERENCES station(station_id)
);

-- Station Reports Table                  
CREATE TABLE Station_Reports (
    event_id BIGSERIAL PRIMARY KEY,
    data_collection_timestamp TIMESTAMP NOT NULL,
    status VARCHAR(50) NOT NULL,
    station INT NOT NULL,
    FOREIGN KEY (station) REFERENCES Station(station_id)
);

-- Sensor Types Table
CREATE TABLE Sensor_Types (
    id INT PRIMARY KEY,
    sensor_type VARCHAR(50) NOT NULL
);

-- Sensor Table
CREATE TABLE Sensor (
    sensor_id INT PRIMARY KEY,
    creation_timestamp TIMESTAMP,
    station INT NOT NULL,
    type INT NOT NULL,
    info TEXT,
    FOREIGN KEY (station) REFERENCES Station(station_id),
    FOREIGN KEY (type) REFERENCES Sensor_Types(id)
);

-- Sensor Data Table
CREATE TABLE Sensor_Data (
    data_id BIGSERIAL PRIMARY KEY,
    data_collection_timestamp TIMESTAMP NOT NULL,
    data VARCHAR(50) NOT NULL,
    sensor INT NOT NULL,
    FOREIGN KEY (sensor) REFERENCES Sensor(sensor_id)
);

-- Actuator Type Table
CREATE TABLE Actuator_Type (
    id INT PRIMARY KEY,
    actuator_type VARCHAR(50) NOT NULL
);

-- Actuator Table
CREATE TABLE Actuator (
    actuator_id INT PRIMARY KEY,
    creation_timestamp TIMESTAMP,
    station INT NOT NULL,
    type INT NOT NULL,
    info TEXT,
    FOREIGN KEY (station) REFERENCES Station(station_id),
    FOREIGN KEY (type) REFERENCES Actuator_Type(id)
);




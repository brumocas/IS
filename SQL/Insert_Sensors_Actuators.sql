--------------------------Production Line-------------------------
INSERT INTO production_line (line_id, type, curr_state)
VALUES (1, 'Wood_Logs', True);

-------------------------Production Line State -------------------
INSERT INTO production_line_state (state)
VALUES (True);
INSERT INTO production_line_state (state)
VALUES (False);

-----------------------------Stations-----------------------------
-- Station 1
INSERT INTO station (station_id, type, prod_line, curr_state)
VALUES (1, 'Pick_Logs', 1, True);
-- Station 2
INSERT INTO station (station_id, type, prod_line, curr_state)
VALUES (2, 'Cut_Logs', 1, True);
-- Station3
INSERT INTO station (station_id, type, prod_line, curr_state)
VALUES (3, 'Manage_Logs', 1, True);
-- Station4
INSERT INTO station (station_id, type, prod_line, curr_state)
VALUES (4, 'Transport_Logs', 1, True);
-- Station5
INSERT INTO station (station_id, type, prod_line, curr_state)
VALUES (5, 'Sort_Logs', 1, True);

-----------------------------Station state-------------------------
INSERT INTO station_state (state)
VALUES (True);
INSERT INTO station_state (state)
VALUES (False);


--------------------------Actuators Types -------------------------
INSERT INTO actuator_type (id, actuator_type)
VALUES (1, 'Manipulator');
INSERT INTO actuator_type (id, actuator_type)
VALUES (2, 'Pump');
INSERT INTO actuator_type (id, actuator_type)
VALUES (3, 'Conveyor');


-----------------------------Actuators-----------------------------
-- Actuator in station 4
INSERT INTO actuator (actuator_id, creation_timestamp , station, type)
VALUES (1, CURRENT_TIMESTAMP, 4, 1);


-- Sensors Types --
INSERT INTO sensor_types (id, sensor_type)
VALUES 
    (1, 'Temperature'),
    (2, 'Humidity'),
    (3, 'Power'),
    (4, 'Luminosity'),
    (5, 'Proximity'),
    (6, 'Force'),
    (7, 'Dimension'),
    (8, 'Gas'),
    (9, 'R'),
    (10, 'G'),
    (11, 'B');


-------------------------------Sensors ----------------------------
-- Sensors Station1
INSERT INTO sensor (sensor_id, creation_timestamp, station, type)
VALUES 
    (1, CURRENT_TIMESTAMP, 1, 1),
    (2, CURRENT_TIMESTAMP, 1, 2),
    (3, CURRENT_TIMESTAMP, 1, 3),
    (4, CURRENT_TIMESTAMP, 1, 4),
    (5, CURRENT_TIMESTAMP, 1, 5);
-- Sensors Station2
INSERT INTO sensor (sensor_id, creation_timestamp, station, type)
VALUES 
    (6, CURRENT_TIMESTAMP, 2, 1),
    (7, CURRENT_TIMESTAMP, 2, 2),
    (8, CURRENT_TIMESTAMP, 2, 3),
    (9, CURRENT_TIMESTAMP, 2, 4),
    (10, CURRENT_TIMESTAMP, 2, 5),
    (11, CURRENT_TIMESTAMP, 2, 7),
    (12, CURRENT_TIMESTAMP, 2, 9),
    (13, CURRENT_TIMESTAMP, 2, 10),
    (14, CURRENT_TIMESTAMP, 2, 11);
-- Sensors Station3
INSERT INTO sensor (sensor_id, creation_timestamp, station, type)
VALUES 
    (15, CURRENT_TIMESTAMP, 3, 1),
    (16, CURRENT_TIMESTAMP, 3, 2),
    (17, CURRENT_TIMESTAMP, 3, 3),
    (18, CURRENT_TIMESTAMP, 3, 4),
    (19, CURRENT_TIMESTAMP, 3, 5),
    (20, CURRENT_TIMESTAMP, 3, 2),
    (21, CURRENT_TIMESTAMP, 3, 6),
    (22, CURRENT_TIMESTAMP, 3, 1),
    (23, CURRENT_TIMESTAMP, 3, 8),
    (24, CURRENT_TIMESTAMP, 3, 4);
-- Sensors Station4
INSERT INTO sensor (sensor_id, creation_timestamp, station, type)
VALUES 
    (25, CURRENT_TIMESTAMP, 4, 1),
    (26, CURRENT_TIMESTAMP, 4, 2),
    (27, CURRENT_TIMESTAMP, 4, 3),
    (28, CURRENT_TIMESTAMP, 4, 4),
    (29, CURRENT_TIMESTAMP, 4, 5);
-- Sensors Station5
INSERT INTO sensor (sensor_id, creation_timestamp, station, type)
VALUES
    (30, CURRENT_TIMESTAMP, 5, 1),
    (31, CURRENT_TIMESTAMP, 5, 2),
    (32, CURRENT_TIMESTAMP, 5, 3),
    (33, CURRENT_TIMESTAMP, 5, 4),
    (34, CURRENT_TIMESTAMP, 5, 5),
    (35, CURRENT_TIMESTAMP, 5, 9),
    (36, CURRENT_TIMESTAMP, 5, 10),
    (37, CURRENT_TIMESTAMP, 5, 11),
    (38, CURRENT_TIMESTAMP, 5, 5),
    (39, CURRENT_TIMESTAMP, 5, 5),
    (40, CURRENT_TIMESTAMP, 5, 5);


-- Alter Sensors and Actuators Text

-- Station1
UPDATE sensor SET info = 'Station Temperature' WHERE sensor_id = 1;
UPDATE sensor SET info = 'Station Humidity' WHERE sensor_id = 2;
UPDATE sensor SET info = 'Station Power' WHERE sensor_id = 3;
UPDATE sensor SET info = 'Station Luminosity' WHERE sensor_id = 4;
UPDATE sensor SET info = 'Station Wood Logs produced' WHERE sensor_id = 5;

-- Station2
UPDATE sensor SET info = 'Station Temperature' WHERE sensor_id = 6;
UPDATE sensor SET info = 'Station Humidity' WHERE sensor_id = 7;
UPDATE sensor SET info = 'Station Power' WHERE sensor_id = 8;
UPDATE sensor SET info = 'Station Luminosity' WHERE sensor_id = 9;
UPDATE sensor SET info = 'Station Wood Logs produced' WHERE sensor_id = 10;
UPDATE sensor SET info = 'Wood Logs Dimension' WHERE sensor_id = 11;
UPDATE sensor SET info = 'Wood Logs R value' WHERE sensor_id = 12;
UPDATE sensor SET info = 'Wood Logs G value' WHERE sensor_id = 13;
UPDATE sensor SET info = 'Wood Logs B value' WHERE sensor_id = 14;

-- Station3
UPDATE sensor SET info = 'Station Temperature' WHERE sensor_id = 15;
UPDATE sensor SET info = 'Station Humidity' WHERE sensor_id = 16;
UPDATE sensor SET info = 'Station Power' WHERE sensor_id = 17;
UPDATE sensor SET info = 'Station Luminosity' WHERE sensor_id = 18;
UPDATE sensor SET info = 'Station Wood Logs produced' WHERE sensor_id = 19;
UPDATE sensor SET info = 'Washing Chamber Humidity' WHERE sensor_id = 20;
UPDATE sensor SET info = 'Drilling Machine Force' WHERE sensor_id = 21;
UPDATE sensor SET info = 'Drying Chamber Temperature' WHERE sensor_id = 22;
UPDATE sensor SET info = 'Gas Chamber Gas' WHERE sensor_id = 23;
UPDATE sensor SET info = 'Curing Chamber Luminosity' WHERE sensor_id = 24;

-- Station4
UPDATE sensor SET info = 'Station Temperature' WHERE sensor_id = 25;
UPDATE sensor SET info = 'Station Humidity' WHERE sensor_id = 26;
UPDATE sensor SET info = 'Station Power' WHERE sensor_id = 27;
UPDATE sensor SET info = 'Station Luminosity' WHERE sensor_id = 28;
UPDATE sensor SET info = 'Station Wood Logs produced' WHERE sensor_id = 29;
UPDATE actuator SET info = 'Transports Wood Logs' WHERE actuator_id = 1;

-- Station5
UPDATE sensor SET info = 'Station Temperature' WHERE sensor_id = 30;
UPDATE sensor SET info = 'Station Humidity' WHERE sensor_id = 31;
UPDATE sensor SET info = 'Station Power' WHERE sensor_id = 32;
UPDATE sensor SET info = 'Station Luminosity' WHERE sensor_id = 33;
UPDATE sensor SET info = 'Station Wood Logs produced' WHERE sensor_id = 34;
UPDATE sensor SET info = 'Wood Log R value' WHERE sensor_id = 35;
UPDATE sensor SET info = 'Wood Log G value' WHERE sensor_id = 36;
UPDATE sensor SET info = 'Wood Log B value' WHERE sensor_id = 37;
UPDATE sensor SET info = 'Cherry Wood Logs' WHERE sensor_id = 38;
UPDATE sensor SET info = 'Pine Wood Logs' WHERE sensor_id = 39;
UPDATE sensor SET info = 'Mahogany Wood Logs' WHERE sensor_id = 40;



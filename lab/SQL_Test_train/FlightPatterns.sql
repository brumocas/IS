-- (C) FEUP SINF M.EEC011 GG & AJS

CREATE SCHEMA student_flight_patterns;
SET search_path = student_flight_patterns;

CREATE TABLE IF NOT EXISTS airports (
    airport integer PRIMARY KEY,
    name character varying(20),
    city character varying(20) NOT NULL,
    country character varying(2)
);

CREATE TABLE IF NOT EXISTS models (
        model character varying(20) primary key,
        manufacturer character varying(20),
        version character varying(20),
        engines integer
);

CREATE TABLE IF NOT EXISTS crafts (
        licence character varying(20) primary key,
        name character varying(20),
        model character varying(20) references models NOT NULL
);

CREATE TABLE IF NOT EXISTS patterns (
        flight integer primary key,
        origin integer references airports,
        destination integer references airports,
        carrier character varying(10),
        duration integer,
        model character varying(20) references models
);

 
INSERT INTO airports VALUES (1,'Sa Carneiro','Porto','PT');
INSERT INTO airports VALUES (3,'Portela','Lisboa','PT');
INSERT INTO airports VALUES (5,'Faro','Faro', 'PT');
INSERT INTO airports VALUES (2,'Madeira','Funchal', 'PT');
INSERT INTO airports VALUES (4,'Ponta Delgada','S. Miguel', 'PT');
INSERT INTO airports VALUES (9,'Orly','Paris','FR');
INSERT INTO airports VALUES (8,'Charles de Gaule','Paris','FR');
INSERT INTO airports VALUES (11,'Heathrow','Londres','UK');
INSERT INTO airports VALUES (12,'Gatwick','Londres','UK');
INSERT INTO airports VALUES (15,'Barajas','Madrid','SP');


INSERT INTO models VALUES (1,'Douglas','DC-10','3');
INSERT INTO models VALUES (2,'Boing','737','2');
INSERT INTO models VALUES (6,'Embraer','E190','2');
INSERT INTO models VALUES (3,'Boing','747','4');
INSERT INTO models VALUES (4,'Airbus','A300','2');
INSERT INTO models VALUES (5,'Airbus','A340','4');
INSERT INTO models VALUES (9,'Airbus','A310','2');


INSERT INTO crafts VALUES ('AA','Scott Adams',1);
INSERT INTO crafts VALUES ('BB','Milo Manara',1);
INSERT INTO crafts VALUES ('CC','Henki Bilal',3);
INSERT INTO crafts VALUES ('DD','Gary Larson',4);
INSERT INTO crafts VALUES ('EE','Bill Waterson',4);
INSERT INTO crafts VALUES ('FF','J R R Tolkien',3);
INSERT INTO crafts VALUES ('GG','Franquin',3);
INSERT INTO crafts VALUES ('JJ','Douglas Adams',1);
INSERT INTO crafts VALUES ('YY','Serpieri',5);


INSERT INTO patterns VALUES (1001,1,2,'TAP',120,1);
INSERT INTO patterns VALUES (1002,2,3,'TAP',60,2);
INSERT INTO patterns VALUES (1010,12,4,'BA',180,3);
INSERT INTO patterns VALUES (1008,3,12,'Portugalia',180,4);
INSERT INTO patterns VALUES (1007,5,1,'TAP',60,5);
INSERT INTO patterns VALUES (1009,1,3,'Portugalia',75,2);
INSERT INTO patterns VALUES (1005,9,2,'AirFrance',120,3);
INSERT INTO patterns VALUES (1003,2,12,'BA',120,5);
INSERT INTO patterns VALUES (1006,8,11,'BA',60,5);
INSERT INTO patterns VALUES (1004,4,3,'SATA',180,6);
INSERT INTO patterns VALUES (1111,1,3,'TAP',120,3);

 

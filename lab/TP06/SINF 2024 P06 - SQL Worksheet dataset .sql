-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--   UP :: FEUP :: M.EEC :: SINF :: asousa@fe.up.pt , gil@fe.up.pt
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--
-- License: https://creativecommons.org/licenses/by/4.0/
-- 
-- EDITED PostgreSQL database dump
-- 

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

-- Adapt the following as needed (or not needed at all)
-- CREATE SCHEMA hosp;
-- ALTER SCHEMA hosp OWNER TO asousa;
-- SET search_path = hosp;

SET default_tablespace = '';
SET default_with_oids = false;

--
-- Name: city; Type: TABLE; Schema: hosp; Tablespace: 
--

CREATE TABLE city (
    name character varying(40) NOT NULL
);

--
-- Name: doctor; Type: TABLE; Schema: hosp;  Tablespace: 
--

CREATE TABLE doctor (
    idcard numeric NOT NULL,
    name character varying(40) NOT NULL,
    start_date date DEFAULT ('now'::text)::date,
    main_contract numeric
);

--
-- Name: COLUMN doctor.start_date; Type: COMMENT; Schema: hosp; 
--

COMMENT ON COLUMN doctor.start_date IS 'start date for contract to main hospital';

--
-- Name: COLUMN doctor.main_contract; Type: COMMENT; Schema: hosp; 
--

COMMENT ON COLUMN doctor.main_contract IS 'main contract to hospital (id)';

--
-- Name: doctor_id_seq; Type: SEQUENCE; Schema: hosp; 
--

CREATE SEQUENCE doctor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

--
-- Name: doctor_id_seq; Type: SEQUENCE OWNED BY; Schema: hosp; 
--

ALTER SEQUENCE doctor_id_seq OWNED BY doctor.idcard;

--
-- Name: hospital; Type: TABLE; Schema: hosp;  Tablespace: 
--

CREATE TABLE hospital (
    name character varying(40) NOT NULL,
    city character varying(40),
    tel character varying(20),
    id numeric NOT NULL
);

--
-- Name: hospital_id_seq; Type: SEQUENCE; Schema: hosp; 
--

CREATE SEQUENCE hospital_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

--
-- Name: hospital_id_seq; Type: SEQUENCE OWNED BY; Schema: hosp; 
--

ALTER SEQUENCE hospital_id_seq OWNED BY hospital.id;

--
-- Name: hospital_speciallity; Type: TABLE; Schema: hosp;  Tablespace: 
--

CREATE TABLE hospital_speciallity (
    spec character varying(4) NOT NULL,
    start_year numeric NOT NULL,
    end_year numeric DEFAULT 0,
    hosp numeric NOT NULL
);

-- ALTER TABLE hospital_speciallity OWNER TO asousa;

--
-- Name: COLUMN hospital_speciallity.spec; Type: COMMENT; Schema: hosp; 
--

COMMENT ON COLUMN hospital_speciallity.spec IS 'speciallity key';

--
-- Name: COLUMN hospital_speciallity.hosp; Type: COMMENT; Schema: hosp; 
--

COMMENT ON COLUMN hospital_speciallity.hosp IS 'hospital id';

--
-- Name: hospital_speciallity_spec_seq; Type: SEQUENCE; Schema: hosp; 
--

CREATE SEQUENCE hospital_speciallity_spec_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

--
-- Name: hospital_speciallity_spec_seq; Type: SEQUENCE OWNED BY; Schema: hosp; 
--

ALTER SEQUENCE hospital_speciallity_spec_seq OWNED BY hospital_speciallity.spec;



--
-- Name: specialty; Type: TABLE; Schema: hosp;  Tablespace: 
--

CREATE TABLE specialty (
    name character varying(40) NOT NULL,
    related character varying(40) DEFAULT NULL::character varying,
    key character varying(4) NOT NULL
);

--
-- Name: COLUMN specialty.related; Type: COMMENT; Schema: hosp; 
--

COMMENT ON COLUMN specialty.related IS 'other related specialties';

--
-- Name: COLUMN specialty.key; Type: COMMENT; Schema: hosp; 
--

COMMENT ON COLUMN specialty.key IS 'specialty shortened';

--
-- Name: id; Type: DEFAULT; Schema: hosp; 
--

ALTER TABLE ONLY hospital ALTER COLUMN id SET DEFAULT nextval('hospital_id_seq'::regclass);

--
-- Data for Name: city; Type: TABLE DATA; Schema: hosp; 
--

INSERT INTO city VALUES ('Porto');
INSERT INTO city VALUES ('Aveiro');
INSERT INTO city VALUES ('Viseu');
INSERT INTO city VALUES ('Faro');
INSERT INTO city VALUES ('Portimao');
INSERT INTO city VALUES ('Braga');
INSERT INTO city VALUES ('Guimaraes');
INSERT INTO city VALUES ('Lisboa');

--
-- Data for Name: doctor; Type: TABLE DATA; Schema: hosp; 
--

INSERT INTO doctor VALUES (9345, 'Florencio', '2016-09-01', 2);
INSERT INTO doctor VALUES (9456, 'Kelli', '2015-01-01', 3);
INSERT INTO doctor VALUES (9567, 'Angela', '2014-01-01', 4);
INSERT INTO doctor VALUES (9678, 'Anna', '2018-05-30', 5);
INSERT INTO doctor VALUES (9789, 'Erica', '2013-01-01', 2);
INSERT INTO doctor VALUES (9901, 'Mary', '2013-01-01', 10);
INSERT INTO doctor VALUES (9001, 'Barbara', '2018-01-01', 5);
INSERT INTO doctor VALUES (9002, 'James', '2011-05-30', 10);
INSERT INTO doctor VALUES (9003, 'Joana', '2012-06-06', 5);
INSERT INTO doctor VALUES (9009, 'Indira', '2002-01-01', 1);
INSERT INTO doctor VALUES (9234, 'Jess', '2017-01-01', 2);
INSERT INTO doctor VALUES (9753, 'Philip', '2003-05-05', 1);
INSERT INTO doctor VALUES (9543, 'Peter', '2004-04-04', 1);

--
-- Name: doctor_id_seq; Type: SEQUENCE SET; Schema: hosp; 
--

SELECT pg_catalog.setval('doctor_id_seq', 1, false);

--
-- Data for Name: hospital; Type: TABLE DATA; Schema: hosp; 
--

INSERT INTO hospital VALUES ('Sao Joao', 'Porto', '22 123 456', 1);
INSERT INTO hospital VALUES ('Santo Antonio', 'Porto', '22 456 789', 2);
INSERT INTO hospital VALUES ('Santa Maria', 'Porto', NULL, 3);
INSERT INTO hospital VALUES ('Hospital Amadora Sintra', 'Lisboa', '21 123 456', 4);
INSERT INTO hospital VALUES ('Hospital Miguel Bombarda', 'Lisboa', '21 123 789', 5);
INSERT INTO hospital VALUES ('Hospital de Curry Cabral', 'Lisboa', '21 321 654', 6);
INSERT INTO hospital VALUES ('Maternidade Dr Alfredo da Costa', 'Lisboa', NULL, 7);
INSERT INTO hospital VALUES ('Hospital de Júlio de Matos', 'Lisboa', NULL, 8);
INSERT INTO hospital VALUES ('Hospital de Sao Teotonio', 'Viseu', NULL, 10);
INSERT INTO hospital VALUES ('Hospital Distrital de Lamego', 'Viseu', NULL, 11);
INSERT INTO hospital VALUES ('Hospital de Candido de Figueiredo', 'Viseu', NULL, 12);
INSERT INTO hospital VALUES ('Hospital da Luz Aveiro', 'Aveiro', NULL, 13);
INSERT INTO hospital VALUES ('Hospital da Criança Maria Pia', 'Porto', NULL, 9);

--
-- Name: hospital_id_seq; Type: SEQUENCE SET; Schema: hosp; 
--

SELECT pg_catalog.setval('hospital_id_seq', 13, true);

--
-- Data for Name: hospital_speciallity; Type: TABLE DATA; Schema: hosp; 
--

INSERT INTO hospital_speciallity VALUES ('F', 2000, 0, 1);
INSERT INTO hospital_speciallity VALUES ('S', 2001, 0, 1);
INSERT INTO hospital_speciallity VALUES ('P', 2000, 0, 1);
INSERT INTO hospital_speciallity VALUES ('P', 1990, 1999, 12);
INSERT INTO hospital_speciallity VALUES ('P', 2005, 0, 12);
INSERT INTO hospital_speciallity VALUES ('G', 1991, 0, 12);
INSERT INTO hospital_speciallity VALUES ('S', 1980, 0, 2);
INSERT INTO hospital_speciallity VALUES ('F', 2009, 0, 2);
INSERT INTO hospital_speciallity VALUES ('P', 2002, 0, 9);
INSERT INTO hospital_speciallity VALUES ('Neo', 2015, 0, 9);
INSERT INTO hospital_speciallity VALUES ('Neo', 1985, 1998, 9);
INSERT INTO hospital_speciallity VALUES ('Neo', 2003, 2005, 9);

--
-- Name: hospital_speciallity_spec_seq; Type: SEQUENCE SET; Schema: hosp; 
--

SELECT pg_catalog.setval('hospital_speciallity_spec_seq', 1, false);

--
-- Data for Name: specialty; Type: TABLE DATA; Schema: hosp; 
--

INSERT INTO specialty VALUES ('General Surgery', NULL, 'S');
INSERT INTO specialty VALUES ('Internal medicine', NULL, 'IM');
INSERT INTO specialty VALUES ('Radiology', NULL, 'R');
INSERT INTO specialty VALUES ('Family Medicine', NULL, 'F');
INSERT INTO specialty VALUES ('Sports Medicine', 'F', 'SM');
INSERT INTO specialty VALUES ('Pediatric infectious diseases', 'P', 'PID');
INSERT INTO specialty VALUES ('Vascular medicine', 'IM', 'VM');
INSERT INTO specialty VALUES ('Interventional radiology', 'R', 'IR');
INSERT INTO specialty VALUES ('Nephrology', 'IM', 'N');
INSERT INTO specialty VALUES ('Geriatrics', 'F', 'G');
INSERT INTO specialty VALUES ('Adolescent medicine', 'P', 'AM');
INSERT INTO specialty VALUES ('Cardiology', 'IM', 'C');
INSERT INTO specialty VALUES ('Cardiothoracic surgery', 'S', 'CS');
INSERT INTO specialty VALUES ('Endocrinology', 'IM', 'E');
INSERT INTO specialty VALUES ('Infectious disease', 'IM', 'ID');
INSERT INTO specialty VALUES ('Plastic surgery', 'S', 'PS');
INSERT INTO specialty VALUES ('Sleep medicine', 'SM', 'Sle');
INSERT INTO specialty VALUES ('Pediatrics', NULL, 'P');
INSERT INTO specialty VALUES ('Pediatric allergology', 'P', 'PA');
INSERT INTO specialty VALUES ('Pediatric oncology', 'P', 'PO');
INSERT INTO specialty VALUES ('Pediatric Hematology', 'P', 'PH');
INSERT INTO specialty VALUES ('Neonatology ', 'P', 'Neo');

--
-- Name: city_pkey; Type: CONSTRAINT; Schema: hosp;  Tablespace: 
--

ALTER TABLE ONLY city
    ADD CONSTRAINT city_pkey PRIMARY KEY (name);

--
-- Name: doctor_pkey; Type: CONSTRAINT; Schema: hosp;  Tablespace: 
--

ALTER TABLE ONLY doctor
    ADD CONSTRAINT doctor_pkey PRIMARY KEY (idcard);

--
-- Name: hospital_pkey; Type: CONSTRAINT; Schema: hosp;  Tablespace: 
--

ALTER TABLE ONLY hospital
    ADD CONSTRAINT hospital_pkey PRIMARY KEY (id);

--
-- Name: hospital_speciallity_pkey; Type: CONSTRAINT; Schema: hosp;  Tablespace: 
--

ALTER TABLE ONLY hospital_speciallity
    ADD CONSTRAINT hospital_speciallity_pkey PRIMARY KEY (spec, start_year, hosp);


--
-- Name: specialty_pkey; Type: CONSTRAINT; Schema: hosp;  Tablespace: 
--

ALTER TABLE ONLY specialty
    ADD CONSTRAINT specialty_pkey PRIMARY KEY (key);

--
-- Name: doctor_main_contract_fkey; Type: FK CONSTRAINT; Schema: hosp; 
--

ALTER TABLE ONLY doctor
    ADD CONSTRAINT doctor_main_contract_fkey FOREIGN KEY (main_contract) REFERENCES hospital(id);

--
-- Name: hospital_city_fkey; Type: FK CONSTRAINT; Schema: hosp; 
--

ALTER TABLE ONLY hospital
    ADD CONSTRAINT hospital_city_fkey FOREIGN KEY (city) REFERENCES city(name);

--
-- Name: hospital_speciallity_hosp_fkey; Type: FK CONSTRAINT; Schema: hosp; 
--

ALTER TABLE ONLY hospital_speciallity
    ADD CONSTRAINT hospital_speciallity_hosp_fkey FOREIGN KEY (hosp) REFERENCES hospital(id);

--
-- Name: hospital_speciallity_spec_fkey; Type: FK CONSTRAINT; Schema: hosp; 
--

ALTER TABLE ONLY hospital_speciallity
    ADD CONSTRAINT hospital_speciallity_spec_fkey FOREIGN KEY (spec) REFERENCES specialty(key);

--
-- Name: specialty_related_fkey; Type: FK CONSTRAINT; Schema: hosp; 
--

ALTER TABLE ONLY specialty
    ADD CONSTRAINT specialty_related_fkey FOREIGN KEY (related) REFERENCES specialty(key);

-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--                  PostgreSQL database dump complete
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

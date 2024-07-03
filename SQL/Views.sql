--------- View for mean sensor values
CREATE VIEW mean_view AS 
(
    SELECT average.s2 AS sensor, average.m2 AS mean, average.std2 AS std, (average.m2 - lat.latest)/average.m2*100 AS diff
    FROM 
    (
        (SELECT sd.sensor AS s2, AVG(CAST(sd.data AS numeric)) AS m2, STDDEV(CAST(sd.data AS numeric)) AS std2
        FROM "Gman21_test".sensor_data AS sd
        GROUP BY sd.sensor) AS average
        JOIN (
            SELECT sd5.sensor, sd5.data::numeric AS latest
            FROM "Gman21_test".sensor_data sd5
            INNER JOIN (
                SELECT sensor, MAX(data_collection_timestamp) as MaxTimestamp
                FROM "Gman21_test".sensor_data
                GROUP BY sensor
            ) latest ON sd5.sensor = latest.sensor AND sd5.data_collection_timestamp = latest.MaxTimestamp
            ) AS lat ON average.s2 = lat.sensor
    )
)
----------


---- Mean power value per station
CREATE VIEW mean_power_all_stations AS
(
    SELECT SUM(avg_per_station.average) AS sum_mean_power
    FROM (
        SELECT s.station AS st, AVG(CAST(sd.data AS numeric)) AS average
        FROM "Gman21_test".sensor_data AS sd
        JOIN "Gman21_test".sensor AS s
        ON s.sensor_id = sd.sensor
        JOIN "Gman21_test".sensor_types AS st
        ON st.id = s.type
        WHERE st.sensor_type = 'Power'
        GROUP BY s.station
    ) AS avg_per_station
)
------

----- Last instantaneous power of all stations
CREATE VIEW instantaneous_power AS
(
    SELECT s.station AS station, sd.data AS power
    FROM "Gman21_test".sensor_data AS sd
    JOIN "Gman21_test".sensor AS s
    ON s.sensor_id = sd.sensor
    JOIN "Gman21_test".sensor_types AS st
    ON st.id = s.type
    JOIN 
    (
        SELECT sd.sensor, MAX(sd.data_collection_timestamp) AS MaxTimestamp
        FROM "Gman21_test".sensor_data AS sd
        JOIN "Gman21_test".sensor AS s
        ON s.sensor_id = sd.sensor
        JOIN "Gman21_test".sensor_types AS st
        ON st.id = s.type
        WHERE st.sensor_type = 'Power'
        GROUP BY sd.sensor
    ) AS max_collection_timestamp
    ON max_collection_timestamp.sensor = s.sensor_id
    WHERE st.sensor_type = 'Power' AND max_collection_timestamp.MaxTimestamp = sd.data_collection_timestamp
    ORDER BY s.station
)

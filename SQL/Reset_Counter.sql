-- Delete Info in the tables
DELETE FROM "Gman21_test"."station_reports";
DELETE FROM "Gman21_test"."sensor_data";
DELETE FROM "Gman21_test"."production_line_state_history";
DELETE FROM "Gman21_test"."station_state_history";

-- Reset Counter --
ALTER SEQUENCE "Gman21_test"."station_reports_event_id_seq" RESTART WITH 1;
ALTER SEQUENCE "Gman21_test"."sensor_data_data_id_seq" RESTART WITH 1;
ALTER SEQUENCE "Gman21_test"."production_line_state_history_id_seq" RESTART WITH 1;
ALTER SEQUENCE "Gman21_test"."station_state_history_id_seq" RESTART WITH 1;

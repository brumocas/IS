------------------------------------------------------------------------------------------------------------
-- Trigger that updates the production line state according to station status

-- Function that the trigger will execute when activated
CREATE OR REPLACE FUNCTION update_production_line()
RETURNS TRIGGER AS $$
DECLARE
    curr_state_trig BOOLEAN;
BEGIN
    -- Check if any of the stations are on (TRUE)
    SELECT EXISTS (
        SELECT 1 FROM "Gman21_test".station WHERE station.curr_state = TRUE
    ) INTO curr_state_trig;

    -- Update production_line table
    UPDATE "Gman21_test".production_line
    SET curr_state = curr_state_trig;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Trigger creation 
CREATE TRIGGER update_production_line_trigger
AFTER INSERT OR UPDATE ON station
FOR EACH ROW
EXECUTE FUNCTION update_production_line();



------------------------------------------------------------------------------------------------------------
-- Trigger that inserts in the production_line_state_history when the curr_state is changed

-- Function that the trigger will execute when activated
CREATE OR REPLACE FUNCTION update_production_line_state_history()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO "Gman21_test".production_line_state_history (line_id, timestamp, state)
    VALUES (NEW.line_id ,CURRENT_TIMESTAMP, NEW.curr_state);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger creation
CREATE TRIGGER production_line_state_history_trigger
AFTER UPDATE ON production_Line
FOR EACH ROW
WHEN (OLD.curr_state IS DISTINCT FROM NEW.curr_state)
EXECUTE FUNCTION update_production_line_state_history();



------------------------------------------------------------------------------------------------------------
-- Trigger that inserts in the station_state_history when the curr_state is changed

-- Function that the trigger will execute when activated
CREATE OR REPLACE FUNCTION update_station_state_history()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO "Gman21_test".station_state_history (station_id, timestamp, state)
    VALUES (NEW.station_id ,CURRENT_TIMESTAMP, NEW.curr_state);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger creation
CREATE TRIGGER station_state_history_trigger
AFTER UPDATE ON station
FOR EACH ROW
WHEN (OLD.curr_state IS DISTINCT FROM NEW.curr_state)
EXECUTE FUNCTION update_station_state_history();

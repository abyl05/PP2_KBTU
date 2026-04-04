#1
CREATE OR REPLACE FUNCTION search_pattern(p TEXT)
RETURNS TABLE(username VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT username, phone
    FROM phonebook
    WHERE username ILIKE '%' || p || '%'
       OR phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

#2
CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, off INT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;

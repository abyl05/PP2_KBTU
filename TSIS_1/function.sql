-- 🔍 SEARCH (name + email + phones)
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(username VARCHAR, email VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.username, c.email, p.phone
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.username ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;


-- 📄 PAGINATION
CREATE OR REPLACE FUNCTION get_contacts_page(lim INT, off INT)
RETURNS TABLE(id INT, username VARCHAR, email VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT id, username, email
    FROM contacts
    ORDER BY id
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;
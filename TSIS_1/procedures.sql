-- 🔁 UPSERT (из Practice 8)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_email VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET email = p_email WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, email)
        VALUES(p_name, p_email);
    END IF;
END;
$$;

-- 📱 ADD PHONE
CREATE OR REPLACE PROCEDURE add_phone(p_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE cid INT;
BEGIN
    SELECT id INTO cid FROM contacts WHERE username = p_name;
    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;

-- 🔄 MOVE TO GROUP
CREATE OR REPLACE PROCEDURE move_to_group(p_name VARCHAR, p_group VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE gid INT;
BEGIN
    SELECT id INTO gid FROM groups WHERE name = p_group;

    IF gid IS NULL THEN
        INSERT INTO groups(name) VALUES(p_group) RETURNING id INTO gid;
    END IF;

    UPDATE contacts SET group_id = gid WHERE username = p_name;
END;
$$;

-- 🗑 DELETE
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE username = p_value OR email = p_value;
END;
$$;
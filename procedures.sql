#1
CREATE OR REPLACE PROCEDURE upsert_user(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE username = p_name;
    ELSE
        INSERT INTO phonebook(username, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


#2
CREATE OR REPLACE PROCEDURE insert_many(names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        
        -- проверка: номер должен быть только цифры
        IF phones[i] ~ '^[0-9]+$' THEN
            INSERT INTO phonebook(username, phone)
            VALUES (names[i], phones[i])
            ON CONFLICT (phone) DO NOTHING;
        ELSE
            RAISE NOTICE 'Invalid phone: %', phones[i];
        END IF;

    END LOOP;
END;
$$;


#3
CREATE OR REPLACE PROCEDURE delete_user(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p_name OR phone = p_phone;
END;
$$;
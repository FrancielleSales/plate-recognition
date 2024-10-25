-- verify_database.sql

--
-- User table checks
--

-- Checks if there is a null field
SELECT *
FROM users
WHERE 
    "name" IS NULL OR
    email IS NULL OR
    password IS NULL;


-- Check if there are repeated fields
SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- List the restrictions defined in the table
SELECT conname, contype
FROM pg_constraint
WHERE conrelid = 'users'::regclass;

--
-- Images table checks
--

-- Checks if there is a null field
SELECT *
FROM images
WHERE
    "name" IS NULL OR
    "path" IS NULL;


-- Check if there are repeated fields
SELECT "name", "path", COUNT(*)
FROM images
GROUP BY "name", "path"
HAVING COUNT(*) > 1;

-- List the restrictions defined in the table
SELECT conname, contype
FROM pg_constraint
WHERE conrelid = 'images'::regclass;

--
-- Results table checks
--

-- Checks if there is a null field
SELECT *
FROM results
WHERE 
    user_id IS NULL OR 
    image_id IS NULL OR 
    x_min IS NULL OR 
    y_min IS NULL OR 
    x_max IS NULL OR 
    y_max IS NULL OR 
    license_plate IS NULL;

-- List the restrictions defined in the table
SELECT conname, contype
FROM pg_constraint
WHERE conrelid = 'results'::regclass;

-- Verify foreign keys
SELECT r.*
FROM results r
LEFT JOIN users u ON r.user_id = u.id
LEFT JOIN images i ON r.image_id = i.id
WHERE u.id IS NULL OR i.id IS NULL;
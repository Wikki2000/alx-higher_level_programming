-- CreateDatabase.sql

-- Check if the database exists
USE hbtn_0c_0;
IF @@ROWCOUNT = 0 THEN
    -- Create the database
    CREATE DATABASE hbtn_0c_0;
END IF;


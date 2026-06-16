#!/usr/bin/env bash
psql -v ON_ERROR_STOP=1 --host $POSTGRES_HOST --username "$POSTGRES_ADMIN_USER" --dbname "$POSTGRES_DB"

set -e

psql -v ON_ERROR_STOP=1 --host postgresql.sandbox.net --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	-- user
	CREATE USER pgadmin WITH PASSWORD '$POSTGRES_USER';
	
	-- create database
	CREATE DATABASE sandboxdb;
	
	-- Grant all access to user
	GRANT ALL PRIVILEGES ON DATABASE sandboxdb TO pgadmin;
	
	-- Grant connect database to user
	GRANT CONNECT ON DATABASE sandboxdb TO pgadmin;
	
	-- Grant connect schema to user
	GRANT USAGE ON SCHEMA public TO pgadmin;
	
	-- Grant read access to all existing tables
	GRANT SELECT ON ALL TABLES IN SCHEMA public TO pgadmin;
	
	-- Grant full access to all existing tables
	GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO pgadmin;

EOSQL

psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'sandboxdb'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE sandboxdb"

DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'sandboxdb') THEN
        PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE sandboxdb');
    END IF;
END $$;


sudo -u postgres psql -c 'SHOW hba_file;'


SELECT table_catalog, table_name, table_schema, table_type 
FROM information_schema.tables 
WHERE table_schema = 'public' 
AND table_type = 'BASE TABLE';

List tables in current schema: \dt
List tables in all schemas: \dt *.*
List with more details: \dt+ (includes size and description).
List tables and views: \d
\connect mysite;
GRANT ALL PRIVILEGES ON SCHEMA public TO mysite;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO mysite;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mysite;

ALTER ROLE mysite CREATEDB;

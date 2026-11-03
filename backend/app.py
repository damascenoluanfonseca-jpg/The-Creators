-- Seed data placeholder for local development.
-- Replace or extend this script based on final requirements.

INSERT INTO destinations (name, country, description) VALUES
    ('Paris', 'France', 'A classic destination for culture, art, and cuisine.'),
    ('Tokyo', 'Japan', 'A vibrant city known for technology, food, and unique neighborhoods.');

INSERT INTO trips (title, destination_id, notes) VALUES
    ('Weekend in Paris', 1, 'Visit museums and walk through historic neighborhoods.'),
    ('Japan exploration', 2, 'Plan a city trip with food and sightseeing ideas.');

-- Arquivo: sql/02_insert_initial_data.sql

-- 1. Inserindo o Satélite
INSERT INTO satellities (id_norad, name, operator)
VALUES (47699, 'Amazonia-1', 'INPE/MCTI');

-- 2. Inserindo a Estação de Solo
INSERT INTO ground_stations (name, latitude, longitude, altitude_meters)
VALUES ('Visiona SJC', -23.1615, -45.7953, 600);
CREATE DATABASE monitoramento_orbital_amazonia1;

CREATE TABLE satellities (
                             id_norad INTEGER PRIMARY KEY,
                             name VARCHAR(50) NOT NULL,
                             operator VARCHAR(100) NOT NULL,
                             is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE ground_stations (
                                 id_gs INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                 name VARCHAR(100) NOT NULL,
                                 latitude DECIMAL(9,6) NOT NULL,
                                 longitude DECIMAL(9,6) NOT NULL,
                                 altitude_meters INTEGER
);

CREATE TABLE pass_predictions (
                                  id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                                  start_utc TIMESTAMPTZ NOT NULL,
                                  end_utc TIMESTAMPTZ NOT NULL,
                                  max_elevation DECIMAL(5,2),
                                  duration_seconds INTEGER,
                                  created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
                                  id_norad INTEGER,
                                  id_gs INTEGER,

                                  CONSTRAINT fk_satellities
                                      FOREIGN KEY (id_norad)
                                          REFERENCES satellities(id_norad)
                                          ON DELETE SET NUL L,

                                  CONSTRAINT fk_ground_stations
                                      FOREIGN KEY (id_gs)
                                          REFERENCES ground_stations(id_gs)
                                          ON DELETE SET NULL
);
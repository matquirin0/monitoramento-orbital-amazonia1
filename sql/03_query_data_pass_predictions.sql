SELECT
    s.name AS satelite,
    gs.name AS estacao,
    TO_CHAR(p.start_utc, 'DD/MM/YYYY HH24:MI') AS inicio_brasilia,
    p.duration_seconds / 60 AS duracao_minutos,
    p.max_elevation AS elevacao_max
FROM pass_predictions p
         JOIN satellities s ON p.id_norad = s.id_norad
         JOIN ground_stations gs ON p.id_gs = gs.id_gs
ORDER BY p.start_utc;
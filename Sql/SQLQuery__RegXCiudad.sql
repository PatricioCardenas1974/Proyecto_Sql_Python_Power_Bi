SELECT Ciudad, COUNT(*) AS total_registros
FROM datos_ventas_directquery
GROUP BY Ciudad;
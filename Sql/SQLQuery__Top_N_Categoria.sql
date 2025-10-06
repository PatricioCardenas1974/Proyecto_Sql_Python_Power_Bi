SELECT TOP 3 Ciudad, COUNT(*) AS ReclamosTotales
FROM datos_ventas_directquery
GROUP BY Ciudad
ORDER BY ReclamosTotales DESC;
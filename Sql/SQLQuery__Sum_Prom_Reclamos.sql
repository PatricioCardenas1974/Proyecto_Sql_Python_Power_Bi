SELECT 
    SUM(ReclamosTotales) AS total_cantidad,
    AVG(ReclamosTotales) AS promedio_cantidad
FROM datos_ventas_directquery;

# Análisis de Datos de una Empresa de Telecomunicaciones usando Python, SQL y Power BI
 
## Vision General

Este proyecto aborda el análisis de una empresa ficticia de Telecomunicaciones en TIEMPO REAL  ( es decir que los campos uno o más de unoi cambiara , por lo tanto se reflejara en suel dashborad).

Datos que pudiesen ser de Ventas, Postventa, Atencion al Cliente Calida, Soporte Tecnico Operaciones, Calidad, Logistica.

Este análisis se centra en la utilizacion de Sql Server para la simulacion de los datos  depositandolos en una base de datos con la participacion de Python en la conexion y creacion de los campos que participan y Power BI para crear un dashboard interactivo, extrayendo los datos desde SQL Server.


## Modelo de Datos

Definir una estructura de datos efectiva en un dashboard es importante; incorporar un modelo de esquema en estrella ofrece un diseño eficiente y hace que la actualización de los datos sea más rápida.

### Campos usadas en el modelo: -

FechaHora DATETIME,
SolicitudesVentas INT,
ConexionesCanceladas INT,
ReclamosTotales INT,
Reclamos24H INT,
Ciudad VARCHAR(50),
CausaReclamo VARCHAR(100),
Vendedor VARCHAR(50),
CanalVenta VARCHAR(50),
EstadoSolicitud VARCHAR(50),
MotivoCancelacion VARCHAR(100),
CausaCancelacion VARCHAR(100),
SolicitudesVE INT,
OrdenesInstPendientes INT,
ConexionesNuevasXCiudad INT

## Desarrollado con:

•[Python](https://www.python.org/)
•[Power BI](https://powerbi.microsoft.com/en-us/)
•[SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)

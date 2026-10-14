# Bases CSV para selección de bridas del tanque flash

Archivos UTF-8 con BOM, separados por coma. Una fila = un registro. Mantener encabezados.

- `corrientes_dwsim.csv`: datos de proceso y velocidades **asumidas** (editables).
- `materiales_b165.csv`: mapeo de especificación y grado al grupo material B16.5.
- `ratings_pt.csv`: **únicamente** fila hasta 38 °C, grupo 2.3, verificada de tabla 2-2.3; no extrapolar.
- `propiedades_ii_d.csv`: esquema vacío para esfuerzos ASME II-D Tabla 1A.
- `especificacion_ii_a.csv`: esquema vacío para características SA-182.
- `dimensiones_bridas.csv`: esquema vacío para combinaciones Clase/NPS/tipo, completar desde tablas B16.5. Cada NPS en su propia fila.
- `tuberias_b3619.csv`: esquema vacío para NPS/schedule, requiere consultar B36.19M.
- `caras_y_acabados.csv`: esquema vacío para caras/acabados.

**Importante:** Las filas PENDIENTE/PLANTILLA no son valores cero. No calcular con campos vacíos ni inferir conformidad ASME. La reproducción completa de tablas ASME sujetas a licencia debe gestionarse conforme a los permisos de uso. No publicar copias extensas de tablas en un repositorio público sin autorización.

**Uso con GitHub:** subir los CSV permitidos a un repositorio, copiar la URL `raw.githubusercontent.com/USUARIO/REPO/RAMA/ruta/archivo.csv`, y pasarla a pandas.read_csv(url). No subir PDFs normativos protegidos sin permiso. Guardar referencias de edición, tabla y notas aplicables.

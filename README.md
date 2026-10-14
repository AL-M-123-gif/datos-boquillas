# CSV para dimensionamiento de bridas del tanque flash V1

Incluye 8 CSV de trabajo con **encabezados compatibles** con el código Colab previo, más `mapa_fuentes.csv`.

## Datos que SÍ existen
- `corrientes_dwsim.csv`: presiones, temperaturas, caudales y velocidades SUPUESTAS de diseño.
- `materiales_b165.csv`: identificación puntual SA-182 F316L, grupo 2.3.
- `ratings_pt.csv`: ratings para grupo 2.3 a temperaturas hasta 38 °C, tomados de la tabla 2-2.3; verificación para otras condiciones es obligatoria.

## Campos aún vacíos
- `dimensiones_bridas.csv`: ASME B16.5-2025 tabla 8 (página 155 de PDF).
- `caras_y_acabados.csv`: ASME B16.5-2025 §6.4 y §6.4.5, Figura 6, Tabla 4.
- `especificacion_ii_a.csv`: BPVC II-A, SA-182/SA-182M.
- `propiedades_ii_d.csv`: BPVC II-D, tabla 1A.
- `tuberias_b3619.csv`: ASME B36.19M no suministrada.

Los campos vacíos significan **NO DISPONIBLE** y nunca deben convertirse en cero o valores inventados.

## Subir a GitHub
1. Extrae el ZIP.
2. En tu repositorio `datos-boquillas`, elige **Add file > Upload files**.
3. Sube los CSV al directorio raíz (no la carpeta).
4. Confirma el commit y comparte `https://github.com/AL-M-123-gif/datos-boquillas`.
5. Cuando el programa consulte, usará `https://raw.githubusercontent.com/AL-M-123-gif/datos-boquillas/main/nombre.csv`.

## Derechos de uso
No se incluye una reproducción masiva de tablas completas ASME. Antes de publicar filas adicionales derivadas de estas normas, comprueba los permisos de reproducción/licencia. Para uso académico local con PDFs licenciados se puede guardar una base privada con extractos autorizados.

## Seguridad
La presión de 5 kPa es absoluta de operación. El rating interno de una brida NO demuestra resistencia al vacío, estanqueidad, diseño de boquilla, refuerzo, cargas de tuberías o cumplimiento BPVC. La selección final requiere revisión de ingeniería.

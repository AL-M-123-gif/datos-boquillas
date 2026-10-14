# Ejemplo de lectura modular para Google Colab
import pandas as pd
BASE_URL = "https://raw.githubusercontent.com/USUARIO/REPOSITORIO/main/bases_bridas_flash/"
ARCHIVOS = ["corrientes_dwsim.csv","materiales_b165.csv","ratings_pt.csv",
 "propiedades_ii_d.csv","especificacion_ii_a.csv",
 "dimensiones_bridas.csv","tuberias_b3619.csv","caras_y_acabados.csv"]
bd = {n.removesuffix(".csv"):pd.read_csv(BASE_URL+n) for n in ARCHIVOS}
print({k:len(v) for k,v in bd.items()})
# Validacion: nunca tratar valores vacios de tablas como cero
clave = bd["dimensiones_bridas"]
if clave["nps"].isna().any() or clave["od_brida_mm"].isna().any():
 print("AVISO: completar tablas dimensionantes antes de calcular bridas.")

import os, re, json, geoip2.database
from geoip2.errors import AddressNotFoundError
from collections import defaultdict

logs_http="D:\\Programacion\\Python\\Estructura_de baces_de_datos\\Corte 3\\Parcial\\Logs"
ruta_base_datos="D:\\Programacion\\Python\\Estructura_de baces_de_datos\\Corte 3\\Parcial\\GeoLite2_base_datos.mmdb"


# Lista donde se almacenará la información extraída
logs_extraidos = []
logs_pais = []

def leer_logs(carpeta_logs):
    patron = re.compile(r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<fecha>[^\]]+)\] "(?P<metodo_http>[A-Z]+) (?P<ruta>\S+)')

    for nombre_archivo in sorted(os.listdir(carpeta_logs)):
        if nombre_archivo.startswith("access_log_"):
            ruta_completa = os.path.join(carpeta_logs, nombre_archivo)
            with open(ruta_completa, 'r') as archivo:
                for linea in archivo:
                    match = patron.search(linea)
                    if match:
                        logs_extraidos.append({
                            "fecha": match.group("fecha"),
                            "ip": match.group("ip"),
                            "metodo_http": match.group("metodo_http"),
                            "ruta": match.group("ruta")
                        })

def reivicion_pais(logs_extraidos, ruta_base_datos):
    reader = geoip2.database.Reader(ruta_base_datos)

    for log in logs_extraidos:
        ip = log.get("ip", "")
        try:
            respuesta = reader.country(ip)
            log["pais"] = respuesta.country.name
        except AddressNotFoundError:
            log["pais"] = "Desconocido"
        except Exception as e:
            log["pais"] = f"Error: {e}"

        logs_pais.append(log)

    reader.close()


def agrupar_por_pais(logs_pais):
    agrupados = defaultdict(list)

    for log in logs_pais:
        pais = log.get('pais', 'Desconocido')
        
        log_sin_pais = {k: v for k, v in log.items() if k != 'pais'}
        
        agrupados[pais].append(log_sin_pais)
    
    return dict(agrupados)

leer_logs(logs_http)
reivicion_pais(logs_extraidos, ruta_base_datos)
agrupados_por_pais = agrupar_por_pais(logs_pais)


with open("Logs_informacion_agrupada_por_pais.json", "w", encoding="utf-8") as f:
    json.dump(agrupados_por_pais, f, ensure_ascii=False, indent=2)
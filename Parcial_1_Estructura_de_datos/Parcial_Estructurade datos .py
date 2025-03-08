import json, re

ips_unicas=set()
fechas={}

def extractFromRegularExpression(regex, data):
  if data:
    return re.findall(regex, data)
  return None

archivo= open("D:\\Programacion\\Python\\Estructura_de baces_de_datos\\Taller_2_uso_de_regex_y_python\\access.log", "r") #en este caso al ser aun ubicacion en el disco se pone en donde tengas el archivo en mi caso es esta 
regex= r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(\d{2}\/\b[a-zA-Z]{3}\b\/\d{4})\:(\d{2}\:\d{2}\:\d{2})\s\+\d{1,4}]\s\"(\b[A-Z]{3,6})\s(\/\S+)\sHTTP\/\d{1}\.\d{1}\"\s(\d{1,3})"
resultado=extractFromRegularExpression(regex, archivo.read())

for ip, fecha, hora, metodo, omitido ,error in resultado:
    if ip not in ips_unicas:
        ips_unicas.add(ip)
        fechas[ip] = (fecha, hora, metodo, omitido, error)
for ip, (fecha, hora, metodo, omitido, error) in fechas.items():
    print(f"La IP {ip} ya la fecha es {fecha} la hora es {hora}  el modo es {metodo} y el error es {error} ")

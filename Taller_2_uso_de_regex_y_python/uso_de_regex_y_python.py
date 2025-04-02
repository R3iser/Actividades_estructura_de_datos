import json, re

def extractFromRegularExpression(regex, achivo):
  if archivo:
    return re.findall(regex, archivo)
  return None

archivo= open("D:\\Programacion\\Python\\Estructura_de baces_de_datos\\Taller_uso_de_regex_y_python\\access.log", "r") #en este caso al ser aun ubicacion en el disco se pone en donde tengas el archivo en mi caso es esta 
regex= r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(\d{2}\/\b[a-zA-Z]{3}\b\/\d{4})\:(\d{2}\:\d{2}\:\d{2})\s\+\d{1,4}](\s\"\b[A-Z]{3,6}\s)"
resultado=extractFromRegularExpression(regex, archivo.read())

for i in range(len(resultado)):
  print(f"la ip{resultado[i][0]} ya la fechaa es {resultado[i][1]}  la hora es {resultado[i][2]} y el modo es{resultado[i][3]}")
# eso si se recomienda paciencia por que se demora lo suya que se escriba todo el archivo XD 

import json

data = {
    "Usuarios": {
        "Trabajadores": [],         #adecirverdad no entendi bien que ise aca o que le movi pero funciono para crear la gerarquia que buscaba :v 
        "Clientes": []
    }
}

#Trabajadores
data["Usuarios"]["Trabajadores"].append({
    "usuario":"01",
    "nombre":"Cristian David",
    "apellido":"Acevedo Hernandez",
    "activo":True,
    "area":"ingenieria(sistemas)",
    "edad":"21",
    "correo":"cdacevedoh@ejemplo.edu.co",
    "cargo":"estudiante",
    "enfermedades fisicas":False,
    "enfermedades mentales":False, 
})
data["Usuarios"]["Trabajadores"].append({
    "usuario":"02",
    "nombre":"",
    "apellido":"",
    "activo":False,
    "area":"",
    "edad":"",
    "correo":"",
    "cargo":"",
    "enfermedades fisicas":False,
    "enfermedades mentales":False, 
})
data["Usuarios"]["Trabajadores"].append({
    "usuario":"03",
    "nombre":"",
    "apellido":"",
    "activo":False,
    "area":"",
    "edad":"",
    "correo":"",
    "cargo":"",
    "enfermedades fisicas":False,
    "enfermedades mentales":False, 
})
data["Usuarios"]["Trabajadores"].append({
    "usuario":"04",
    "nombre":"",
    "apellido":"",
    "activo":False,
    "area":"",
    "edad":"",
    "correo":"",
    "cargo":"",
    "enfermedades fisicas":False,
    "enfermedades mentales":False, 
})

#Clientes
data["Usuarios"]["Clientes"].append({
    "usuario":"101",
    "nombre":"Laura Daniela",
    "apellido":"Albarrasin",
    "activo":True,
    "vip":True,
    "edad":"20",
    "correo":"ldalbarrasin@gmail.com",
    "tipo de pago":"targeta",
    "Tipo de targeta":"credito",
    "enfermedades mentales":False, 
})
data["Usuarios"]["Clientes"].append({
    "usuario":"102",
    "nombre":"",
    "apellido":"",
    "activo":False,
    "vip":False,
    "edad":"",
    "correo":"@gmail.com",
    "tipo de pago":"",
    "Tipo de targeta":"",
    "enfermedades mentales":False, 
})
data["Usuarios"]["Clientes"].append({
    "usuario":"102",
    "nombre":"",
    "apellido":"",
    "activo":False,
    "vip":False,
    "edad":"",
    "correo":"@gmail.com",
    "tipo de pago":"",
    "Tipo de targeta":"",
    "enfermedades mentales":False, 
})


with open('informacion.json', 'w') as f:
    json.dump(data,f,indent=4)

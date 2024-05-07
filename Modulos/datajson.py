import json 

with open('Reportes_Consulta_API/Datos_completos_clima.json', 'r') as f:
    datos = json.load(f)


def consultTempAct(datajson):

    for dia in datajson['days']:
        temp = dia['temp']
query_cost = datos['queryCost']
resolved_address = datos['resolvedAddress']



print("Ciudad actual:", resolved_address)

for dia in datos['days']:
    fecha = dia['datetime']
    temp_max = dia['tempmax']
    temp_min = dia['tempmin']
    temp = dia['temp']
    precip_prob = dia['precipprob']
    conditions = dia['conditions']

    print("\nFecha:", fecha)
    print("Temperatura Máxima:", temp_max)
    print("Temperatura Mínima:", temp_min)
    print("Temperatura del dia:", temp)
    print("Probabilidad de Precipitación:", precip_prob)
    print("Condiciones:", conditions)

    # Extraer datos por hora
    for hora in dia['hours']:
        hora_del_dia = hora['datetime']
        temperatura = hora['temp']
        precipitacion = hora['precip']


        print("\tHora:", hora_del_dia)
        print("\tTemperatura:", temperatura)
        print("\tPrecipitación:", precipitacion)

 


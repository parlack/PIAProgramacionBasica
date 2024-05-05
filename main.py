import json
import sys

import requests


def menu(menuPrin):
  print('\tMenú:')
  print('1. Consultas web')
  print('2. Consultas de registros')
  print('3. Estadísticas')
  print('4. Gráficas')
  print('5. Borrar todo ')
  print('6. Salir ')



ciudad = input('Ingrese su ciudad: ')
i = 0
while i < len(ciudad):
    carac = ciudad[i]
    if  (ord(carac)>=48 and ord(carac)<=57):
        print ('Indique una ciudad válida')
        ciudad = input('Ingrese su ciudad:\n')


ciudadtoapi = ciudad.replace(' ','%20')
response = requests.request("GET", f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{ciudadtoapi}?unitGroup=metric&include=hours%2Calerts%2Cevents%2Ccurrent%2Cdays&key=UMWHQ8PEMQ54XH8C2SU2RNVPS&contentType=json")

if response.status_code!=200:
  print('Unexpected Status code: ', response.status_code)
  sys.exit()  

jsonData =  json.dumps(response.json(),indent=4)
with open('Reportes_Consulta_API/Datos.json', 'w') as archivo:
  archivo.write(jsonData)





#print(jsonData)
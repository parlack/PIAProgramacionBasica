import json
import sys
import re
import urllib.request
from colorama import Fore, Back, Style, init
import requests

def ValLetrasYespacios(cadena):
    i=0
    state=True
    while i<len(cadena) and state==True:
        caracter=cadena[i]
        if (ord(caracter)>=65 and ord(caracter)<=90) or (ord(caracter)==32) or (ord(caracter)>=97 and ord(caracter)<=122):
            state=True
        else:
            state=False
        i+=1
        
    if state:
        return False
    else:
        return True   
    
def requestAPI(city):
    ciudadtoapi = city.replace(' ','%20')
    response = requests.request("GET", f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{ciudadtoapi}?unitGroup=metric&include=hours%2Calerts%2Cevents%2Ccurrent%2Cdays&key=UMWHQ8PEMQ54XH8C2SU2RNVPS&contentType=json")

    if response.status_code!=200:
        print(Fore.RED,'Unexpected Status code: ', response.status_code,Style.RESET_ALL)  
        print('Intente nuevamente:')
        requestAPI(input('Ingrese ciudad a consultar: '))
    else:
      jsonData =  json.dumps(response.json(),indent=4)
      with open('Reportes_Consulta_API/Datos_completos_clima.json', 'w') as archivo:
        archivo.write(jsonData)

def ValRangoNums(inicio,fin,numero):

    try:
      int(numero)
    except:
      return False
    
    if re.match(rf'[{inicio}-{fin}]', numero):
        return True
    else:
        return False

def check_internet_connection():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.error.URLError:
        return False

def menus(numbermenu):

  match numbermenu:
    case 1:
      print(Fore.BLUE,'\tMenú:',Style.RESET_ALL)
      print('1. Consultas web')
      print('2. Consultas de registros')
      print('3. Estadísticas')
      print('4. Gráficas')
      print('5. Borrar todo ')
      print('6. Salir ')
      resp=input('Ingrese la opcion del menu: ')
      while ValRangoNums(1,6,resp)==False:
        print('Respuesta invalida, ingrese una opcion correcta')
        resp=input('Ingrese la opcion del menu: ')
      return int(resp)
    
    case 2:
      print(Fore.BLUE,'\tConsultas web:',Style.RESET_ALL)
      print('1. Temperatura Actual:')
      print('2. Temperatura de las proximas 12 horas:')
      print('3. Consultar Temperatura minimas y Maximas de los siguientes dias:')
      print('4. Consultar probabilidad de precipitacion de los siguientes dias:')
      print('5. Cambiar de ciudad')
      print('6. Ir a menu principal ') 
      resp=input('Ingrese la opcion del menu: ')
      while ValRangoNums(1,6,resp)==False:
        print('Respuesta invalida, ingrese una opcion correcta')
        resp=input('Ingrese la opcion del menu: ')
      return int(resp)
    
    case 3:
      print(Fore.BLUE,'\tConsultas de registros:',Style.RESET_ALL)
      print('1. Temperatura Estimada Actual:')
      print('2. Temperatura de las proximas 12 horas:')
      print('3. Consultar Temperatura minimas y Maximas de los siguientes dias:')
      print('4. Consultar probabilidad de precipitacion de los siguientes dias:')
      print('5. Ir a menu principal ') 
      resp=input('Ingrese la opcion del menu: ')
      while ValRangoNums(1,5,resp)==False:
        print('Respuesta invalida, ingrese una opcion correcta')
        resp=input('Ingrese la opcion del menu: ')
      return int(resp)
     
    case 4:
      print(Fore.BLUE,'\tEstadísticas:',Style.RESET_ALL)
      print('1. Promedio de temperaturas')
      print('2. Promedio de humedad')
      print('3. Promedio de radiacion solar')
      print('4. Promedio de indice uv')
      print('5. Dia con mayor temperatura')
      print('6. Dia con menor temperatura')
      print('7. Ir a menu principal ') 
      resp=input('Ingrese la opcion del menu: ')
      while ValRangoNums(1,7,resp)==False:
        print('Respuesta invalida, ingrese una opcion correcta')
        resp=input('Ingrese la opcion del menu: ')
      return int(resp)
     
    case 5:
      print('\Gráficas:')

    case 6:
      print('\Borrar todo:')

    
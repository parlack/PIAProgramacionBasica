import re
import urllib.request
import os
from colorama import Fore, Style, init


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

def borrar_archivos_en_carpeta(ruta_carpeta):

    archivos = os.listdir(ruta_carpeta)
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)
            print(f"Se ha borrado {ruta_archivo}")

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
      print(Fore.BLUE,'\tGráficas:',Style.RESET_ALL)
      print('1. Grafica lineal Temperaturas por hora')
      print('2. Grafica de barras temperatura por dia')
      print('3. Grafica lineal de humedad')
      print('4. Grafica lineal probabilidad de precipitacion')
      print('5. Grafica lineal indice UV')
      print('6. Ir a menu principal')
      resp=input('Ingrese la opcion del menu: ')
      while ValRangoNums(1,6,resp)==False:
        print('Respuesta invalida, ingrese una opcion correcta')
        resp=input('Ingrese la opcion del menu: ')
      return int(resp)
    

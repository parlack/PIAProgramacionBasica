import Modulos.module1 as modd
import Modulos.manejo_datajson as datas
from colorama import Fore, Style, init

if __name__ == '__main__':
  if modd.check_internet_connection():
    Internet=True
    dafaultcity='Monterrey'
    print(f'Ciudad por default: {dafaultcity}')
    datas.requestAPI(dafaultcity)
  else:
    print(Fore.RED,'Error al cargar datos,Favor de conectarse a internet para tener los datos mas actualizados, se trabajara con los ultimos datos actualizados',Style.RESET_ALL)
    print('La ciudad con registros es:', datas.getcity())
    Internet=False

  resp=modd.menus(1)
  while resp!=6:
    match resp:
      case 1:
        if Internet:
          datas.requestAPI(input('Ingrese ciudad a consultar: '))
          resp1=modd.menus(2)
          while resp1!=6:

            print('Ciudad registrada:', datas.getcity())

            match resp1:
              case 1:
                print(Fore.GREEN,'La temperatura actual es:',str(datas.consultTempAct())+'°C',Style.RESET_ALL)
              case 2:
                datas.Climaprox12h()
              case 3:
                datas.temperaturasMinYmaxXdia()
              case 4:
                datas.probprecipitacionxdia()
              case 5:
                datas.requestAPI(input('Ingrese ciudad a consultar: '))
                print('Ciudad registrada:', datas.getcity())
            resp1=modd.menus(2)
        else:
          print(Fore.RED,'Error al cargar datos,Favor de conectarse a internet para tener los datos mas actualizados, se trabajara con los ultimos datos actualizados',Style.RESET_ALL)



      case 2:
        try:
          print('La ciudad con registros es:', datas.getcity())
          print('Ultima actualizacion de registros:',datas.fechas(1))

          if datas.checardiasfecha()==False:
            print(Fore.RED,'No se puede obtener informacion actual debido a que los registros son muy antiguos')
            print('Favor de conectarse a internet y actualizarlos',Style.RESET_ALL)
          else:
            resp2=modd.menus(3)
            while resp2!=5:
              match resp2:
                case 1:
                  print(Fore.GREEN,'La temperatura estimada actual estimada es:',str(datas.consultTempActEst())+'°C',Style.RESET_ALL)
                case 2:
                  datas.Climaprox12h()
                case 3:
                  datas.temperaturasMinYmaxXdia()
                case 4:
                  datas.probprecipitacionxdia()
              resp2=modd.menus(3)
        except:
          print(Fore.RED,'Error al abrir los registros, favor de conectarse a internet y actualizarlos lo antes posible',Style.RESET_ALL)

      case 3:
        try:
          print('El registro de fecha que se tiene es desde',datas.fechas(1),'hasta',datas.fechas(15))
          print('La ciudad con registros es:', datas.getcity())
          resp3=modd.menus(4)
          while resp3!=7:
            match resp3:
              case 1:
                print(Fore.GREEN,'Promedio de Temperatura:', datas.estadisticas(1),Style.RESET_ALL)
              case 2:
                print(Fore.GREEN,'Promedio de Humedad:',datas.estadisticas(2),Style.RESET_ALL)
              case 3:
                print(Fore.GREEN,'Promedio de radiacion solar:',datas.estadisticas(3),Style.RESET_ALL)
              case 4:
                print(Fore.GREEN,'Promedio de indice uv:', datas.estadisticas(4),Style.RESET_ALL)
              case 5:
                print(Fore.GREEN,'El dia con mayor temperatura es:',str(datas.estadisticas(5)[0])+',','con una temperatura de',str(datas.estadisticas(5)[1])+'°C',Style.RESET_ALL)
              case 6:
                print(Fore.GREEN,'El dia con menor temperatura es:',str(datas.estadisticas(6)[0])+',','con una temperatura de',str(datas.estadisticas(6)[1])+'°C',Style.RESET_ALL)

            resp3=modd.menus(4)
        except:
          print(Fore.RED,'Error al abrir los registros, favor de conectarse a internet y actualizarlos lo antes posible',Style.RESET_ALL)

      case 4:
        
        try:
          resp4=modd.menus(5)
          while resp4!=6:
            match resp4:
              case 1:
                datas.graficas(1)
                
              case 2:
                datas.graficas(2)
              
              case 3:
                datas.graficas(3)
                
              case 4:
                datas.graficas(4)
                
              case 5:
                datas.graficas(5)
            resp4=modd.menus(5)
        except Exception as e:
          print(Fore.RED,'Error al abrir los registros, favor de conectarse a internet y actualizarlos lo antes posible',Style.RESET_ALL)
          print(e)

      case 5:
        modd.menus(6)
        modd.borrar_archivos_en_carpeta('Graficas')
        modd.borrar_archivos_en_carpeta('Reportes_Consulta_API')
        modd.borrar_archivos_en_carpeta('Reportes_datos_numéricos')
        
    resp=modd.menus(1)
    
  if modd.check_internet_connection():
    Internet=True
    dafaultcity='Monterrey'
    print(f'Ciudad por default: {dafaultcity}')
    datas.requestAPI(dafaultcity)
  else:
    print(Fore.RED,'Error al cargar datos,Favor de conectarse a internet para tener los datos mas actualizados, se trabajara con los ultimos datos actualizados',Style.RESET_ALL)
    print('La ciudad con registros es:', datas.getcity())
    Internet=False

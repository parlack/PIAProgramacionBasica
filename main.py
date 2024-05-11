import Modulos.moduless as modd
import Modulos.datajson as datas
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
            resp1=modd.menus(2)
        else:
          print('Ciudad registrada:', datas.getcity())


      case 2:

        print('La ciudad con registros es:', datas.getcity())
        print('Ultima actualizacion de registros:',datas.fechas(1))

        if datas.checardiasfecha()==False:
          print('No se puede obtener informacion actual debido a que los registros son muy antiguos')
          print('Favor de conectarse a internet y actualizarlos')
        else:
          resp2=modd.menus(3)
          while resp2!=5:
            match resp2:
              case 1:
                print('La temperatura estimada actual estimada es:',str(datas.consultTempActEst())+'°C')
              case 2:
                datas.Climaprox12h()
              case 3:
                datas.temperaturasMinYmaxXdia()
              case 4:
                datas.probprecipitacionxdia()
            resp2=modd.menus(3)

      case 3:
        print('El registro de fecha que se tiene es desde',datas.fechas(1),'hasta',datas.fechas(15))
        resp3=modd.menus(4)
        while resp3!=7:
          match resp3:
            case 1:
              print('Promedio de Temperatura:', datas.PromTempProxDias())
            case 2:
              print('Promedio de Humedad:',datas.PromHumedadProxDias())
            case 3:
              print('Promedio de radiacion solar:',datas.PromRadiacionSolar())
            case 4:
              print('Promedio de indice uv:', datas.PromIndiceuv())
            case 5:
              print('El dia con mayor temperatura es:',str(datas.diaMayorTemperatura()[0])+',','con una temperatura de',str(datas.diaMayorTemperatura()[1])+'°C')
            case 6:
              print('El dia con menor temperatura es:',str(datas.diamenorTemperatura()[0])+',','con una temperatura de',str(datas.diamenorTemperatura()[1])+'°C')

          resp3=modd.menus(4)
      case 4:
        modd.menus(5)

      case 5:
        modd.menus(6)
      

    resp=modd.menus(1)

import Modulos.moduless as modd
import Modulos.datajson as datas

if modd.check_internet_connection():
  dafaultcity='Monterrey'
  print(f'Ciudad por default: {dafaultcity}')
  modd.requestAPI(dafaultcity)
else:
  print('Error al cargar datos,Favor de conectarse a internet para tener los datos mas actualizados, se trabajara con los ultimos datos actualizados')

resp=modd.menus(1)
while resp!=6:
  match resp:
    case 1:
      modd.requestAPI(input('Ingrese ciudad a consultar: '))
      resp1=modd.menus(2)
      while resp1!=6:

    
        match resp1:
          case 1:
            print('La temperatura estimada actual estimada es:',str(datas.consultTempActEst())+'°C')
        
          case 2:
            datas.Climaprox12h()

          case 3:
            datas.temperaturasMinYmaxXdia()
          case 4:
            datas.probprecipitacionxdia()
        resp1=modd.menus(2)



    case 2:
      
      modd.menus(3)

    case 3:
      modd.menus(4)

    case 4:
      modd.menus(5)

    case 5:
      modd.menus(6)


  resp=modd.menus(1)

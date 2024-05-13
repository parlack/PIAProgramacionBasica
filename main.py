# Importación de módulos y bibliotecas necesarias
import Modulos.module1 as modd  # Importa el módulo 'module1' con el alias 'modd'
import Modulos.manejo_datajson as datas  # Importa el módulo 'manejo_datajson' con el alias 'datas'
from colorama import Fore, Style, init  # Importa clases para manejar colores en la terminal

# Verifica si este script es el principal
if __name__ == '__main__':
    # Verifica la conexión a Internet
    if modd.check_internet_connection():
        Internet = True
        default_city = 'Monterrey'  # Ciudad predeterminada
        print(f'Ciudad por default: {default_city}')
        datas.requestAPI(default_city)  # Realiza una solicitud a la API para obtener datos
    else:
        # Mensaje de error si no hay conexión a Internet
        print(Fore.RED, 'Error al cargar datos, Favor de conectarse a internet para tener los datos más actualizados, se trabajará con los últimos datos actualizados', Style.RESET_ALL)
        print('La ciudad con registros es:', datas.getcity())
        Internet = False

    # Muestra el menú principal y realiza acciones según la opción seleccionada
    resp = modd.menus(1)
    while resp != 6:
        match resp:
            # Opción 1: Consultas web
            case 1:
                if Internet:
                    # Realiza consultas web si hay conexión a Internet
                    datas.requestAPI(input('Ingrese ciudad a consultar: '))
                    resp1 = modd.menus(2)
                    while resp1 != 6:
                        print('Ciudad registrada:', datas.getcity())
                        match resp1:
                            case 1:
                                print(Fore.GREEN, 'La temperatura actual es:', str(datas.consultTempAct()) + '°C', Style.RESET_ALL)
                            case 2:
                                datas.Climaprox12h()
                            case 3:
                                datas.temperaturasMinYmaxXdia()
                            case 4:
                                datas.probprecipitacionxdia()
                            case 5:
                                datas.requestAPI(input('Ingrese ciudad a consultar: '))
                                print('Ciudad registrada:', datas.getcity())
                        resp1 = modd.menus(2)
                else:
                    # Mensaje de error si no hay conexión a Internet
                    print(Fore.RED, 'Error al cargar datos, Favor de conectarse a internet para tener los datos más actualizados, se trabajará con los últimos datos actualizados', Style.RESET_ALL)

            # Opción 2: Consultas de registros
            case 2:
                try:
                    print('La ciudad con registros es:', datas.getcity())
                    print('Última actualización de registros:', datas.fechas(1))
                    if datas.checardiasfecha() == False:
                        # Mensaje de advertencia si los registros son antiguos
                        print(Fore.RED, 'No se puede obtener información actual debido a que los registros son muy antiguos')
                        print('Favor de conectarse a internet y actualizarlos', Style.RESET_ALL)
                    else:
                        resp2 = modd.menus(3)
                        while resp2 != 5:
                            match resp2:
                                case 1:
                                    print(Fore.GREEN, 'La temperatura estimada actual estimada es:', str(datas.consultTempActEst()) + '°C', Style.RESET_ALL)
                                case 2:
                                    datas.Climaprox12h()
                                case 3:
                                    datas.temperaturasMinYmaxXdia()
                                case 4:
                                    datas.probprecipitacionxdia()
                            resp2 = modd.menus(3)
                except:
                    # Mensaje de error si hay problemas al abrir los registros
                    print(Fore.RED, 'Error al abrir los registros, favor de conectarse a internet y actualizarlos lo antes posible', Style.RESET_ALL)

            # Opción 3: Estadísticas
            case 3:
                try:
                    print('El registro de fecha que se tiene es desde', datas.fechas(1), 'hasta', datas.fechas(15))
                    print('La ciudad con registros es:', datas.getcity())
                    resp3 = modd.menus(4)
                    while resp3 != 7:
                        match resp3:
                            case 1:
                                print(Fore.GREEN, 'Promedio de Temperatura:', datas.estadisticas(1), Style.RESET_ALL)
                            case 2:
                                print(Fore.GREEN, 'Promedio de Humedad:', datas.estadisticas(2), Style.RESET_ALL)
                            case 3:
                                print(Fore.GREEN, 'Promedio de radiación solar:', datas.estadisticas(3), Style.RESET_ALL)
                            case 4:
                                print(Fore.GREEN, 'Promedio de indice uv:', datas.estadisticas(4), Style.RESET_ALL)
                            case 5:
                                print(Fore.GREEN, 'El día con mayor temperatura es:', str(datas.estadisticas(5)[0]) + ',', 'con una temperatura de', str(datas.estadisticas(5)[1]) + '°C', Style.RESET_ALL)
                            case 6:
                                print(Fore.GREEN, 'El día con menor temperatura es:', str(datas.estadisticas(6)[0]) + ',', 'con una temperatura de', str(datas.estadisticas(6)[1]) + '°C', Style.RESET_ALL)
                        resp3 = modd.menus(4)
                except:
                    # Mensaje de error si hay problemas al abrir los registros
                    print(Fore.RED, 'Error al abrir los registros, favor de conectarse a internet y actualizarlos lo antes posible', Style.RESET_ALL)

            # Opción 4: Gráficas
            case 4:
                try:
                    resp4 = modd.menus(5)
                    while resp4 != 6:
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
                        resp4 = modd.menus(5)
                except Exception as e:
                    # Mensaje de error si hay problemas al abrir los registros
                    print(Fore.RED, 'Error al abrir los registros, favor de conectarse a internet y actualizarlos lo antes posible', Style.RESET_ALL)
                    print(e)

            # Opción 5: Borrar archivos
            case 5:
                modd.menus(6)
                # Borra archivos en carpetas específicas
                modd.borrar_archivos_en_carpeta('Graficas')
                modd.borrar_archivos_en_carpeta('Reportes_Consulta_API')
                modd.borrar_archivos_en_carpeta('Reportes_datos_numéricos')

        # Vuelve a mostrar el menú principal
        resp = modd.menus(1)

    # Verifica nuevamente la conexión a Internet al finalizar el script para intentar actualizar los datos
    if modd.check_internet_connection():
        Internet = True
        default_city = 'Monterrey'
        print(f'Ciudad por default: {default_city}')
        datas.requestAPI(default_city)
    else:
        print(Fore.RED, 'Error al cargar datos, Favor de conectarse a internet para tener los datos más actualizados, la siguiente ves se trabajará con los últimos datos actualizados', Style.RESET_ALL)
        print('La ciudad con registros es:', datas.getcity())
        Internet = False


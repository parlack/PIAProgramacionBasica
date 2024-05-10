import json 
import pytz
from datetime import datetime
import Widgets as wg

def data():
    with open('Reportes_Consulta_API/Datos_completos_clima.json', 'r') as f:
        datos = json.load(f)
    return datos



def getcity():
    return data()['address']

def ultimafecha():
    ultimodia=''
    for dia in data()['days']:
        ultimodia = dia['datetime']
    return ultimodia
        

def getdatecalendar():
    timezone = data()['timezone']
    tz = pytz.timezone(timezone)
    datafechaact = datetime.now(tz)
    fechaact=str(datafechaact.strftime('%Y-%m-%d'))
    fecha_d_m_aa  = str(wg.getdatecalendar(fechaact,ultimafecha())) 
    fecha_datetime = datetime.strptime(fecha_d_m_aa, "%d/%m/%y")
    fecha_aaaa_mm_dd = fecha_datetime.strftime("%Y-%m-%d")
    return fecha_aaaa_mm_dd


def consultTempActEst():
    timezone = data()['timezone']
    tz = pytz.timezone(timezone)
    datafechaact = datetime.now(tz)
    fechaact=str(datafechaact.strftime('%Y-%m-%d'))
    horaact=str(datafechaact.strftime('%H:00:00'))

def consultTempAct():

    return data()['currentConditions']['temp']




def temperaturasMinYmaxXdia():
    fechaconsulta=getdatecalendar()
    for dia in data()['days']:
        fecha = dia['datetime']
        if fecha==fechaconsulta:
            print(f'Dia: {fechaconsulta}')
            print('Min:',dia['tempmin'],'\t Max:',dia['tempmax'])
            break

def probprecipitacionxdia():
    fechaconsulta=getdatecalendar()

    for dia in data()['days']:
        fecha = dia['datetime']
        if fecha==fechaconsulta:
            precip_prob = dia['precipprob']
            print(f'La probabilidad de precipitacion del dia {fechaconsulta} es:',str(precip_prob)+'%')
            

def Climaprox12h():
    timezone = data()['timezone']
    tz = pytz.timezone(timezone)
    datafechaact = datetime.now(tz)

    horaact=int(datafechaact.strftime('%H'))
    cambiodia=0;
    for i in range(12):
        horafecha=horaact+i
        formatohora=str(str(horafecha).zfill(2))
        horacamparativa=formatohora+':00:00'

        if horafecha==23:
            horaact=horafecha-24-i
            cambiodia+=1
            
        for dia in data()['days']:
            diaa=int(datafechaact.strftime('%d'))+cambiodia
            formatodia=str(str(diaa).zfill(2))

            fechaact=str(datafechaact.strftime(f'%Y-%m-{formatodia}'))
            fecha = dia['datetime']
            if fecha==fechaact:
                
                for time in dia['hours']:
                    hora_del_dia = time['datetime']

                    if horacamparativa==hora_del_dia:
                        Temp= time['feelslike']
                        print(f'{fecha},{hora_del_dia}')
                        print('Temperatura:',Temp)
                        
         
print(consultTempAct())

import json 
import pytz
from datetime import datetime
import re

with open('Reportes_Consulta_API/Datos_completos_clima.json', 'r') as f:
    datos = json.load(f)


def consultTempActEst():

    timezone = datos['timezone']
    tz = pytz.timezone(timezone)
    datafechaact = datetime.now(tz)
    fechaact=str(datafechaact.strftime('%Y-%m-%d'))
    horaact=str(datafechaact.strftime('%H:00:00'))

    temp=0;
    for dia in datos['days']:
        fecha = dia['datetime']
        if fecha==fechaact:
            for time in dia['hours']:
                hora_del_dia = time['datetime']
                if horaact==hora_del_dia:
                    temp= time['feelslike']
                    return temp
                    

def probprecipitaciondia():
    timezone = datos['timezone']
    tz = pytz.timezone(timezone)
    datafechaact = datetime.now(tz)
    fechaact=str(datafechaact.strftime('%Y-%m-%d'))

    for dia in datos['days']:
        fecha = dia['datetime']
        if fecha==fechaact:
            precip_prob = dia['precipprob']
            return precip_prob
                
def probprecipitacionprox12h():
    timezone = datos['timezone']
    tz = pytz.timezone(timezone)
    datafechaact = datetime.now(tz)
    fechaact=str(datafechaact.strftime('%Y-%m-%d'))
    horaact=str(datafechaact.strftime('%H:00:00'))

 









 


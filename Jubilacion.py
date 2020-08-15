import streamlit as st
from enum import Enum
from typing import List

def jubilacion(sueldo_clp,tasa,tiempo_años,capital_actual,sexo):
    
    for i in range(0,(tiempo_años*12)+1):
        
        if i==0:
            aporte = ((sueldo_clp/0.83)*(1+0.01/12))*0.1 + capital_actual
        else:
            aporte = ((sueldo_clp/0.83)*(1+0.01/12))*0.1 + monto_ganado 
        monto_ganado = aporte * (1+tasa/1200)
        #print(monto_ganado)
        
    if sexo=='Hombre':
        pension_mensual = monto_ganado/(20*12)
    else:
        pension_mensual = monto_ganado/(30*12)
    return f'{round(pension_mensual):,}',monto_ganado

def jubilacion_total(sueldo_clp,tasa,tiempo_años,capital_actual):
    
    for i in range(0,(tiempo_años*12)+1):
        
        if i==0:
            aporte = ((sueldo_clp/0.83)*(1+0.01/12))*0.1  + capital_actual
        else:   
            aporte = ((sueldo_clp/0.83)*(1+0.01/12))*0.1 + monto_ganado
        monto_ganado = aporte * (1+tasa/1200)
        print(monto_ganado)
        
    return f'{round(monto_ganado):,}'

st.write("""
# AFP y Jubilación """)

st.sidebar.header('Parámetros')
sexo = st.sidebar.selectbox("Sexo", ('Hombre','Mujer'))
sueldo_liquido = st.sidebar.number_input('Cuánto es su sueldo líquido?')
rentabilidad = st.sidebar.number_input('Tasa de Rentabilidad')
tiempo_jubilacion = st.sidebar.number_input('Cuánto le queda para Jubilar?')
capital_actual = st.sidebar.number_input('Cuánto es su capital actual?')
pensound = jubilacion(sueldo_liquido,rentabilidad,int(tiempo_jubilacion),capital_actual, sexo)
pensound_2 = jubilacion_total(sueldo_liquido,rentabilidad,int(tiempo_jubilacion),capital_actual)
st.write( "Su pensión mensual será **{}** y su monto total acumulado es **{}**.".format(pensound,pensound_2))







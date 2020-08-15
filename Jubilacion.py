import streamlit as st

st.write("""

# AFP y Jubilación """)

def jubilacion(sueldo_clp,tasa,tiempo_años,capital_actual,sexo):
    
    for i in range(0,(tiempo_años*12)+1):
        
        if i==0:
            aporte = (sueldo_clp/0.83)*0.1 + capital_actual
        else:
            aporte = (sueldo_clp/0.83)*0.1 + monto_ganado
        monto_ganado = aporte * (1+tasa/1200)
        #print(monto_ganado)
        
    if sexo=='h':
        pension_mensual = monto_ganado/(21*12)
    else:
        pension_mensual = monto_ganado/(31*12)
    return f'{pension_mensual:,}'

    
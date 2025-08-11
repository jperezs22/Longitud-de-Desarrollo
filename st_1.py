import streamlit as st
from math import sqrt

st.title("Calculo de Longitud de Desarrollo - ACI 318")

normativa = st.selectbox("Elige una Normativa", ["ACI-318-14", "ACI-318-19"])


if normativa == "ACI-318-19":
    st.write("Propiedas de Materiales:")
    fy = st.number_input("fy",value=60000)
    fc = st.number_input("f'c",value=3000)

    # Entradas del usuario
    st.write("Factores de Modificacion:")
    w_e = st.selectbox("ψe", [1.2,1.0])
    w_r = st.selectbox("ψr", [1.0,1.6])
    w_o = st.selectbox("ψo", [1.0,1.25])
    w_c = st.selectbox("ψc", [round(fc/15000 + 0.6, 2),1.0])

    st.write("Diametro de Barra:")
    d_b = st.selectbox("Elige el Diametro a Usar",[3/8,1/2,5/8,3/4,1])

    st.write("Resultado (cm):")
    ldh = (fy*w_e*w_r*w_o*w_c/(55*sqrt(fc)))*d_b**1.5
    if ldh < 6:
        st.write(f"La longitud de desarrollo para #{d_b*8:.0f} es: {6*2.54:.2f} cm")
    else:
        st.write(f"La longitud de desarrollo para #{d_b*8:.0f} es: {ldh*2.54:.2f} cm")
else:
    st.write("Propiedas de Materiales:")
    fy = st.number_input("fy",value=60000)
    fc = st.number_input("f'c",value=3000)

    # Entradas del usuario
    st.write("Factores de Modificacion:")
    w_e = st.selectbox("ψe", [1.2,1.0])
    w_c = st.selectbox("ψc", [0.7,1.0])
    w_r = st.selectbox("ψr", [0.8,1.0])

    st.write("Diametro de Barra:")
    d_b = st.selectbox("Elige el Diametro a Usar",[3/8,1/2,5/8,3/4,1])

    st.write("Resultado (cm):")
    ldh = (fy*w_e*w_r*w_c/(50*sqrt(fc)))*d_b
    if ldh < 6:
        st.write(f"La longitud de desarrollo para #{d_b*8:.0f} es: {6*2.54:.2f} cm")
    else:
        st.write(f"La longitud de desarrollo para #{d_b*8:.0f} es: {ldh*2.54:.2f} cm")



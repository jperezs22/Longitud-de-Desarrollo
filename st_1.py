import streamlit as st
from math import sqrt

st.title("Calculo de Longitud de Desarrollo con Gancho - ACI 318")
normativa = st.selectbox("Elige una Normativa:", ["ACI-318-14", "ACI-318-19"],)

if normativa == "ACI-318-19":
    st.write("**Propiedas de Materiales:**")
    fy = st.number_input("fy (psi)",min_value= 30000, max_value= 60000,value=60000,step=30000)
    fc = st.number_input("f'c (psi)",min_value=3000, max_value=6000, value=3000, step=500)

    # Entradas del usuario
    st.write("**Factores de Modificacion:**")
    w_e = st.selectbox("ψe", [1.2,1.0], help="1.2: Refuerzo con recubrimiento epoxico o zinc y Barras con recubrimiento dual de zinc y epoxico. " \
    "                  \n\n1.0: Refuerzo sin recubrimiento o refuerzo recubierto con zinc (galvanizado).*" )
    w_r = st.selectbox("ψr", [1.0,1.6],help=    "1.0: Para Barras #11 y menores con Ath>=0.4Ahs o s>=6db."
                                                "\n\n1.6: Otros Casos.")
    w_o = st.selectbox("ψo", [1.0,1.25], help="1.0: Para Barras con Ganchos de diametro #11 y menores: "
                 "(1) Terminando dentro del nucleo de la columna con un rec. lateral, perpendicular al plano del gancho, mayor o igual a 2.5in ó" 
                 "(2) Con recubrimiento Lateral, perpendicular al plano del gancho, mayor o igual a 6db" 
                 "\n\n 1.25: Otros Casos.")
    w_c = st.selectbox("ψc", [round(fc/15000 + 0.6, 2),1.0], help="f'c/15000 + 0.6: Para f'c < 6000psi."
                      "\n\n 1.0: Para f'c >= 6000psi.")

    st.write("**Diametro de Barra:**")
    d_b = st.selectbox("Elige el Diametro a Usar",[3/8,1/2,5/8,3/4,1])

    st.write("**Resultado (cm):**")
    ldh = (fy*w_e*w_r*w_o*w_c/(55*sqrt(fc)))*d_b**1.5
    if ldh < 6:
        st.write(f"La longitud de desarrollo para #{d_b*8:.0f} es: {6*2.54:.2f} cm")
    else:
        st.write(f"La longitud de desarrollo para #{d_b*8:.0f} es: {ldh*2.54:.2f} cm")
else:
    st.write("**Propiedas de Materiales:**")
    fy = st.number_input("fy (psi)",min_value= 30000, max_value= 60000,value=60000,step=30000)
    fc = st.number_input("f'c (psi)",min_value=3000, max_value=6000, value=3000, step=500)

    # Entradas del usuario
    st.write("**Factores de Modificacion:**")
    w_e = st.selectbox("ψe", [1.2,1.0], help="1.2: Refuerzo con recubrimiento epoxico o zinc y barras con recubrimiento dual de zinc y epoxico."
                       "\n\n1.0: Refuerzo sin recubrimiento o refuerzo recubierto con zinc (galvanizado).")
    w_c = st.selectbox("ψc", [0.7,1.0],help="1.2: Para ganchos de barras #11 y menores, con recubrimiento lateral(normal al plano del gancho) >= 2.5in y"
                "para ganchos de 90 grados con recubrimiento en la extension de la barra mas alla del gancho >= 2in*"
                "\n\n1.0: Otros Casos.")
    w_r = st.selectbox("ψr", [0.8,1.0],help="0.8: Para ganchos de 90 grados de barras #11 y menores y que se encuentran:"
    "             (1) confinados a lo largo de ldh con estribos perpendiculares a ldh con s <= 3db, o bien,"
    "             (2) confinados a lo largo de la barra que se esta desarrollando mas alla del gancho"
    "                 por estribos perpendiculares a lext con s <= 3db."
    "                 \n\nPara ganchos de 180 grados de barra #11 y menores que se encuentran confinados con estribos"
    "                 perpendiculares a lext con s <= 3db."
    "                 \n\n1.0: Otros Casos.")

    st.write("**Diametro de Barra:**")
    d_b = st.selectbox("Elige el Diametro a Usar",[3/8,1/2,5/8,3/4,1])

    st.write("**Resultado (cm):**")
    ldh = (fy*w_e*w_r*w_c/(50*sqrt(fc)))*d_b
    if ldh < 6:
        st.write(f"La longitud de desarrollo para #{d_b*8:.0f} es: {6*2.54:.2f} cm")
    else:
        st.write(f"La longitud de desarrollo para #{d_b*8:.0f} es: {ldh*2.54:.2f} cm")



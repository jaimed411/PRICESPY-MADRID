import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Cargar el modelo entrenado
model = joblib.load(r'/workspaces/probando/data/MODEL3.sav')

# Función para hacer una predicción con el modelo
def predict_price(features):
    return model.predict([features])[0]

# Configurar el tema de la aplicación con colores fríos
st.set_page_config(
    page_title="Predicción de Precio de Propiedades",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Encabezado de la aplicación con un título atractivo
st.title('Predicción de Precio de Propiedades en Madrid')

# Sidebar con opciones de entrada y colores personalizados
st.sidebar.header('Ingrese las características de la propiedad')
st.sidebar.markdown('**Por favor, complete los siguientes campos:**')

# Crear widgets para las características de entrada
euros_per_m2 = st.sidebar.number_input('Euros/m2', min_value=0, max_value=10000, step=1)
baños = st.sidebar.number_input('Baños', min_value=0, max_value=10, step=1)
metros_cuadrados = st.sidebar.number_input('Metros cuadrados construidos', min_value=0, max_value=1000, step=1)
habitaciones = st.sidebar.number_input('Habitaciones', min_value=0, max_value=10, step=1)
planta = st.sidebar.number_input('Planta', min_value=0, max_value=10, step=1)

# Crear un mapeo para mostrar "Sí" y "No" en lugar de 0 y 1
si_no_mapping = {0: "No", 1: "Sí"}

# Utilizar el mapeo en los selectboxes
terraza = st.sidebar.selectbox('Terraza', [0, 1], format_func=lambda x: si_no_mapping[x])
aire_acondicionado = st.sidebar.selectbox('Aire acondicionado', [0, 1], format_func=lambda x: si_no_mapping[x])
trastero = st.sidebar.selectbox('Trastero', [0, 1], format_func=lambda x: si_no_mapping[x])
piscina = st.sidebar.selectbox('Piscina', [0, 1], format_func=lambda x: si_no_mapping[x])
parking_incluido = st.sidebar.selectbox('Parking incluído', [0, 1], format_func=lambda x: si_no_mapping[x])
jardin = st.sidebar.selectbox('Jardín', [0, 1], format_func=lambda x: si_no_mapping[x])
parking = st.sidebar.selectbox('Parking', [0, 1], format_func=lambda x: si_no_mapping[x])
ascensor = st.sidebar.selectbox('Ascensor', [0, 1], format_func=lambda x: si_no_mapping[x])
obra_nueva = st.sidebar.selectbox('Obra nueva', [0, 1], format_func=lambda x: si_no_mapping[x])

# Crear un diccionario con las características ingresadas
input_features = {
    'Jardín (Sí/No)': jardin,
    'Parking incluído (Sí/No)': parking_incluido,
    'Obra nueva (Sí/No)': obra_nueva,
    'Trastero (Sí/No)': trastero,
    'Ascensor (Sí/No)': ascensor,
    'Piscina (Sí/No)': piscina,
    'Terraza (Sí/No)': terraza,
    'Parking (Sí/No)': parking,
    'Aire acondicionado (Sí/No)': aire_acondicionado,
    'Habitaciones': habitaciones,
    'Baños': baños,
    'Euros/m2': euros_per_m2,
    'Metros cuadrados construidos': metros_cuadrados,
    'Planta': planta,
}

# Hacer una predicción con el modelo
if all(value == 0 for value in input_features.values()):
    predicted_price = 0.0
else:
    predicted_price = predict_price(list(input_features.values()))

# Mostrar el precio predicho en la aplicación con estilo
st.subheader('Precio Estimado de la Propiedad')
st.write(f'El precio estimado de la propiedad es: {predicted_price:.2f} Euros')
st.markdown('**Nota:** Los resultados son estimaciones basadas en el modelo.')

# Pie de página con información adicional
st.sidebar.markdown('---')
st.sidebar.text('Desarrollado por: Tu Nombre')
st.sidebar.text('Fecha: Septiembre 2023')

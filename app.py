import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Anuncios de venta de vehículos en los Estados Unidos')

# Crear un histograma

hist_button = st.checkbox('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Boton para construir grafico de dispersion

scatter_button = st.checkbox(
    'Construir diagrama de dispersion')  # crear un botón

if scatter_button:
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de vehículos')

    # crear el diagrama de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # Mostrar diagrama de dispersión
    st.plotly_chart(fig, use_container_width=True)

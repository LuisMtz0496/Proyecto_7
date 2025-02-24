import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Carritos")

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
build_histogram = st.checkbox('Construir un histograma') # casillas de verificación
build_disp = st.checkbox('Construir gráfico de dispersión')  # crear un botón

if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Construir un histograma para la columna odómetro')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_disp:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
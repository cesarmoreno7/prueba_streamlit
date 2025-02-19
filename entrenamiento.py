import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Agroindustria en Colombia",
    page_icon="🌿",
    layout="wide"
)

# Título del Dashboard
st.title("🌿 Agroindustria en Colombia")
st.sidebar.title("📊 Opciones de Visualización")

# Generación de datos aleatorios (150 filas x 8 columnas)
np.random.seed(42)
data = pd.DataFrame({
    "Región": np.random.choice(["Andina", "Caribe", "Pacífica", "Orinoquía", "Amazonía"], 150),
    "Producción (Toneladas)": np.random.randint(1000, 50000, 150),
    "Área Sembrada (ha)": np.random.randint(50, 1000, 150),
    "Costo de Producción ($)": np.random.randint(50000, 5000000, 150),
    "Precio de Venta ($)": np.random.randint(1000, 20000, 150),
    "Consumo de Agua (m³)": np.random.randint(500, 10000, 150),
    "Empleo Generado": np.random.randint(10, 500, 150),
    "Exportaciones ($)": np.random.randint(10000, 1000000, 150)
})

# Selección de variables para graficar
st.sidebar.subheader("Seleccionar variables:")
x_axis = st.sidebar.selectbox("Eje X", data.columns[1:])
y_axis = st.sidebar.selectbox("Eje Y", data.columns[1:])

# Gráfico interactivo con Plotly
fig = px.scatter(data, x=x_axis, y=y_axis, color="Región", title=f"{x_axis} vs {y_axis}")

st.plotly_chart(fig)


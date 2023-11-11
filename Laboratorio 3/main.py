import pandas as pd
import plotly.express as px

# Dataset
data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

nuevos_colores = ['blue', 'green', 'orange', 'red', 'purple', 'pink', 'lime', 'cyan', 'magenta', 'gold', 'silver', 'maroon', 'olive', 'navy', 'yellow']

color_map = dict(zip(df['materia'].unique(), nuevos_colores))

fig_pie = px.pie(df, names='aprobado', title="Gráfico de Torta", color='aprobado', color_discrete_map={"Sí": 'lime', 'No': 'red'})
fig_pie.show()

fig_box = px.box(df, x="materia", y="nota", title="Gráfico de Cajas", color="materia", color_discrete_map=color_map)
fig_box.show()

import pandas as pd
import matplotlib.pyplot as plt

def plot_boxplot(datos):
    datos['materia'] = pd.Categorical(datos['materia'], categories=orden_materias, ordered=True)

    boxprops = dict(linewidth=2, color='blue')
    medianprops = dict(linestyle='-', linewidth=2.5, color='red')
    datos.boxplot(column='nota', by='materia', grid=False, boxprops=boxprops, medianprops=medianprops)
    plt.title('Distribución de Notas de Estudiantes por Materia')
    plt.suptitle('')
    plt.xlabel('Materia')
    plt.ylabel('Notas')
    plt.show()

def plot_pie_chart(datos):
    aprobados = datos[datos['aprobado'] == 'Sí'].shape[0]
    no_aprobados = datos[datos['aprobado'] == 'No'].shape[0]

    etiquetas = 'Aprobados', 'No Aprobados'
    tamaños = [aprobados, no_aprobados]
    colores = ['lightgreen', 'lightcoral']

    plt.pie(tamaños, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=45, explode=(0.1, 0))
    plt.axis('equal')
    plt.title('Distribución de Resultados')
    plt.show()

# Dataset
data = {
    'id': list(range(1, 21)),
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'] * 5,
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

# Materias
orden_materias = ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje']

# DataFrame de Pandas
df = pd.DataFrame(data)

# Llamar las funciones
plot_boxplot(df)
plot_pie_chart(df)

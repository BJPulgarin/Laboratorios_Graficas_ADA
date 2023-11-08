import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

def GraficoDispersion():
    plt.scatter(matematicas, ciencias, color='Blue')
    plt.title('Relación entre las calificaciones de Matemáticas y Ciencias')
    plt.xlabel('Calificaciones de Matemáticas')
    plt.ylabel('Calificaciones de Ciencias')
    plt.show()

def GraficoErrorbar():
    x = ['Matemáticas', 'Ciencias', 'Literatura']
    y = [matematicas.mean(), ciencias.mean(), literatura.mean()]
    minimos = [errores_matematicas[0], errores_ciencias[0], errores_literatura[0]]
    maximos = [errores_matematicas[1], errores_ciencias[1], errores_literatura[1]]
    print(y)
    print(minimos)
    print(maximos)
    plt.errorbar(x, y, yerr=[minimos, maximos], fmt='o', capsize=5, label='Promedio')
    plt.title('Calificaciones promedio con barras de error')
    plt.xlabel('Materias')
    plt.ylabel('Calificaciones promedio')
    plt.legend()
    plt.show()

def Histograma():
    plt.hist(matematicas)
    plt.title('Distribución de las calificaciones de Matemáticas')
    plt.xlabel('Calificaciones de Matemáticas')
    plt.ylabel('Frecuencia')
    plt.show()

GraficoDispersion()
GraficoErrorbar()
Histograma()

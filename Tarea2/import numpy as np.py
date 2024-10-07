import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Generar 100 números aleatorios uniformemente distribuidos entre 0 y 1
np.random.seed(42)  # Para reproducibilidad
data = np.random.uniform(0, 1, 100)

# Realizar la prueba de Kolmogorov-Smirnov
D, p_value = stats.kstest(data, 'uniform')

# Imprimir los resultados
print(f"Estadístico D: {D}")
print(f"Valor p: {p_value}")

# Interpretar el resultado
alpha = 0.05
if p_value < alpha:
    print("Rechazamos la hipótesis nula: los datos no siguen una distribución uniforme.")
else:
    print("No rechazamos la hipótesis nula: los datos podrían seguir una distribución uniforme.")

# Graficar los datos
plt.hist(data, bins=10, density=True, alpha=0.6, color='g', label='Datos aleatorios')
plt.title('Histograma de Números Aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

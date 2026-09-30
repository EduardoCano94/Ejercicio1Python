import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
datos = pd.read_csv("01-student-por.csv")

print(datos.head())


# Análisis de G3
g3 = datos["G3"]

media = g3.mean()
mediana = g3.median()
moda = g3.mode()[0]

desviacion = g3.std()
rango = g3.max() - g3.min()

Q1 = g3.quantile(0.25)
Q3 = g3.quantile(0.75)
IQR = Q3 - Q1

print("\nEstadísticas de G3")
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Desviación estándar:", desviacion)
print("Rango:", rango)
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)


# Histograma de las calificaciones finales
plt.figure(figsize=(8, 5))
plt.hist(g3, bins=10, edgecolor="black")

plt.title("Distribución de las calificaciones finales (G3)")
plt.xlabel("Calificación final (G3)")
plt.ylabel("Frecuencia")

plt.show()


# Análisis de las ausencias
absences = datos["absences"]

Q1_abs = absences.quantile(0.25)
Q3_abs = absences.quantile(0.75)
IQR_abs = Q3_abs - Q1_abs

limite_inferior = Q1_abs - 1.5 * IQR_abs
limite_superior = Q3_abs + 1.5 * IQR_abs

outliers = datos[
    (absences < limite_inferior) |
    (absences > limite_superior)
]

print("\nAnálisis de ausencias")
print("Q1:", Q1_abs)
print("Q3:", Q3_abs)
print("IQR:", IQR_abs)
print("Límite inferior:", limite_inferior)
print("Límite superior:", limite_superior)
print("Número de outliers:", len(outliers))
print("Valores atípicos:", outliers["absences"].tolist())


# Histograma de las ausencias
plt.figure(figsize=(8, 5))
plt.hist(absences, bins=15, edgecolor="black")

plt.title("Distribución de las ausencias")
plt.xlabel("Número de faltas")
plt.ylabel("Frecuencia")

plt.show()


# Tiempo de estudio y calificación final
medianas_studytime = datos.groupby("studytime")["G3"].median()

print("\nMediana de G3 según tiempo de estudio")
print(medianas_studytime)

plt.figure(figsize=(8, 5))

datos.boxplot(column="G3", by="studytime")

plt.title("Nota final (G3) según tiempo de estudio")
plt.suptitle("")
plt.xlabel("Tiempo de estudio (studytime)")
plt.ylabel("Calificación final (G3)")

plt.show()


# Consumo de alcohol y calificación final
medianas_walc = datos.groupby("Walc")["G3"].median()

print("\nMediana de G3 según consumo de alcohol")
print(medianas_walc)

plt.figure(figsize=(8, 5))

datos.boxplot(column="G3", by="Walc")

plt.title("Nota final (G3) según consumo de alcohol en fin de semana")
plt.suptitle("")
plt.xlabel("Consumo de alcohol (Walc)")
plt.ylabel("Calificación final (G3)")

plt.show()


# Correlaciones entre las calificaciones
correlaciones = datos[["G1", "G2", "G3"]].corr()

print("\nCorrelación entre G1, G2 y G3")
print(correlaciones)


# Relación entre G1 y G3
plt.figure(figsize=(8, 5))

plt.scatter(datos["G1"], datos["G3"])

plt.title("Relación entre G1 y G3")
plt.xlabel("Nota del primer periodo (G1)")
plt.ylabel("Nota final (G3)")

plt.show()


# Relación entre ausencias y G3
correlacion_absences_g3 = datos["absences"].corr(datos["G3"])

print("\nCorrelación entre ausencias y G3")
print(correlacion_absences_g3)

plt.figure(figsize=(8, 5))

plt.scatter(datos["absences"], datos["G3"])

plt.title("Relación entre ausencias y calificación final")
plt.xlabel("Número de faltas")
plt.ylabel("Calificación final (G3)")

plt.show()
import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

#Respuesta 1 - Consumo promedio hogar casa 5

print(f"Respuesta 1: {consumo[4][4]}")

#Respuesta 2 - consumo de los ultimos 3 horas el domingo
print(f"Respuesta 2: {consumo[-3:, -1]}")

#Respuesta 3 - consumo promedio fines de semana

promedio_total_fines_semana = np.mean(consumo[:,5:])
print(f"Respuesta 3: {promedio_total_fines_semana}")

#Respuesta 4 - mayor desviacion estandar
desviacion_dia = np.std(consumo, axis=0)
indice = np.argmax(desviacion_dia)
print(f"Respuesta 4: (indice){indice} : (valor){desviacion_dia[indice]}")

#Esto indica que el consumo de energia en ese dia varia bastante

#Respuesta 5 - los 3 hogares con menor consumo y sus indices

total_hogar = np.sum(consumo, axis=1)
indices = np.argsort(total_hogar)[:3]

print(f"Respuesta 5: (indices){indices} : (valores){total_hogar[indices]}")

#Respuesta 6 - hogar 3 con 10% mas de consumo

hogar3 = consumo[2]
hogar3_10p = hogar3 * 1.10
total_hogar3_10p = np.sum(hogar3_10p)

print(f"Respuesta 6: {total_hogar3_10p}")

import pandas as pd
import matplotlib.pyplot as plt
# Iram Jimenez NC = 0079
# 4. Leer el archivo CSV desde el archivo de indian food
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV Iram Jimenez 0079 ---")
print(df_food_india)
print("\n--- Mostrar nombre de comida mas ingredientes Iram Jimenez 0079 ---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- Tiempo de cocinado mostrar los primeros 10 registros Iram Jimenez 0079 ---")
nombre_y_tiempo = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_tiempo)

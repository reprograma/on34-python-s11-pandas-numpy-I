import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./temperatura_RJ.csv', encoding='utf-8', delimiter=',')

estatistica_descritiva = df['Temperatura'].describe()
print("""
    Estatística Descritiva:
""", estatistica_descritiva
)

plt.figure(figsize=(12, 4))
plt.plot(df['Hora'], df['Temperatura'], marker='*', linestyle='-', color='r')
plt.title('Temperatura no Decorrer das Horas')
plt.xlabel('Hora')
plt.ylabel('Temperatura')
plt.xticks(range(24))
plt.grid(True)
plt.show()

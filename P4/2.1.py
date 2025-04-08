import pandas as pd
import matplotlib.pyplot as plt


file_path = "GAMES.csv"
df = pd.read_csv(file_path, delimiter=';', encoding='utf-8', on_bad_lines='skip', header=None)

df.columns = ['title', 'genre', 'link', 'year']
df = df.dropna(subset=['year', 'genre'])
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df = df[df['year'] > 1970]


plt.figure(figsize=(12, 6))
df['year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Количество выпущенных игр по годам')
plt.xlabel('Год')
plt.ylabel('Количество игр')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

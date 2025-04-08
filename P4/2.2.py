import pandas as pd
import matplotlib.pyplot as plt


file_path = "GAMES.csv"
df = pd.read_csv(file_path, delimiter=';', encoding='utf-8', on_bad_lines='skip', header=None)

df.columns = ['title', 'genre', 'link', 'year']
df = df.dropna(subset=['year', 'genre'])
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df = df[df['year'] > 1970]
genre_year = df.groupby(['year', 'genre']).size().unstack(fill_value=0)
genre_year.plot(kind='bar', stacked=True, colormap='tab20', figsize=(14, 8))
plt.title('Популярность жанров по годам')
plt.xlabel('Год')
plt.ylabel('Количество игр')
plt.legend(title='Жанр', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

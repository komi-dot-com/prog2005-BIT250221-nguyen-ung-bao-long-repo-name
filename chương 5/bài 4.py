import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('california_cities.csv')
top10_cities = df.sort_values(by='area_total_km2', ascending=False).head(10)

plt.barh(top10_cities['city'], top10_cities['area_total_km2'])
plt.title('Top 10 Thành phố lớn nhất California theo Diện tích')
plt.xlabel('Diện tích (km2)')
plt.ylabel('Thành phố')
plt.gca().invert_yaxis()
plt.show()

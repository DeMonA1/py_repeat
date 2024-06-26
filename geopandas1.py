import geopandas
import matplotlib.pyplot as plt


world = geopandas.read_file("C:\\Users\\Дима\\Downloads\\ne_110m_admin_0_countries\\ne_110m_admin_0_countries.shp")
cities = geopandas.read_file('C:\\Users\\Дима\\Downloads\\ne_110m_populated_places\\ne_110m_populated_places.shp')
base = world.plot(color='orchid')
cities.plot(ax=base, color='blue', markersize=1)
plt.show()

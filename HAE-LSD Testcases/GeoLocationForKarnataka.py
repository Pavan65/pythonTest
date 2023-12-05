import geopandas as gpd
import matplotlib.pyplot as plt

# Load the India map shapefile
india = gpd.read_file("C:\\Users\\pekabath\\Downloads\\gadm41_IND_1.json\\gadm41_IND_1.json")  # Replace with the actual path to your India shapefile

# Filter Karnataka from the India map
karnataka = india[india['NAME_1'] == 'Karnataka']

# Plot the India map
ax = india.plot(figsize=(10, 10), color='lightgray', edgecolor='black')
#ax1 = karnataka.plot(figsize=(10, 10), color='none', edgecolor='red', linewidth=2)


# Plot the outline of Karnataka
karnataka.plot(ax=ax, color='none', edgecolor='red', linewidth=2)

# Set plot title
plt.title('India Map with Karnataka Outline')

# Adjust the aspect ratio based on the bounding box
#x_min, y_min, x_max, y_max = india.total_bounds
#ax.set_xlim(x_min, x_max)
#ax.set_ylim(y_min, y_max)

# Show the plot
plt.show()
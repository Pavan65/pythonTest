import geopandas as gpd
import matplotlib.pyplot as plt

# Load the India map shapefile
india = gpd.read_file("C:\\Users\\pekabath\\Downloads\\gadm41_IND_1.json\\gadm41_IND_1.json")
print("print starts\n")
print(india.columns)
print("print ends\n")
# Filter Tamil Nadu from the India map
#tamil_nadu = india[india['NAME_1'] == 'Tamil Nadu']
tamil_nadu = india[india['HASC_1'] == 'IN.TN']

# Plot the India map
ax = india.plot(figsize=(10, 10), color='lightgray', edgecolor='black')

# Plot the outline of Tamil Nadu if available
if not tamil_nadu.empty:
    tamil_nadu.boundary.plot(ax=ax, color='red', linewidth=2)

# Set plot title
plt.title('India Map with Tamil Nadu Outline')

# Show the plot
plt.show()

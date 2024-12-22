import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
#ex 1
points = [[3, -5], [-6, 6], [6, -4], [5, -5], [9, 10]]

vor = Voronoi(points)

fig, ax = plt.subplots(figsize=(8, 8))

voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='red', line_width=2)

ax.plot([p[0] for p in points], [p[1] for p in points], 'bo', label="Points")

ax.set_xlim(-12, 15)
ax.set_ylim(-12, 15)
ax.set_aspect('equal', 'box')
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc="upper left")
ax.set_title("Voronoi Diagram")

plt.show()

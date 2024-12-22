import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np

def triangulation_info(points):
    """
    Computes the number of triangles and edges in the triangulation of a given set of points;
    """
    delaunay = Delaunay(points)

    num_triangles = len(delaunay.simplices)

    edges = set()
    for simplex in delaunay.simplices:
        edges.add(tuple(sorted([simplex[0], simplex[1]])))
        edges.add(tuple(sorted([simplex[1], simplex[2]])))
        edges.add(tuple(sorted([simplex[2], simplex[0]])))
    num_edges = len(edges)

    return num_triangles, num_edges

def plot_triangulation(points):
    """
    Plots the Delaunay triangulation for visualization;
    """
    delaunay = Delaunay(points)
    plt.triplot(points[:, 0], points[:, 1], delaunay.simplices, color='red')
    plt.plot(points[:, 0], points[:, 1], 'bo', label="Points")
    plt.title("Delaunay Triangulation")
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

lambda_val = 0  # Adjust this for different values of λ
points = np.array([
    [1, 1],    # A
    [1, -1],   # B
    [-1, -1],  # C
    [-1, 1],   # D
    [0, -2],   # E
    [0, lambda_val]  # M
])

num_triangles, num_edges = triangulation_info(points)
print(f"Number of Triangles: {num_triangles}")
print(f"Number of Edges: {num_edges}")

plot_triangulation(points)

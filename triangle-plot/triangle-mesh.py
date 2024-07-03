import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import json

# Example JSON data for the triangles
triangles_json = '''
[
    [
        { "x": 1, "y": -1, "z": 1.375 },
        { "x": 2, "y": -0.6666666666666667, "z": 1.5 },
        { "x": 2, "y": 3, "z": 1.5 }
    ],
    [
        { "x": 2, "y": -0.6666666666666667, "z": 1.5 },
        { "x": 3, "y": -0.33333333333333337, "z": 1.5 },
        { "x": 2, "y": 3, "z": 1.5 }
    ],
    [
        { "x": 3, "y": -0.33333333333333337, "z": 1.5 },
        { "x": 3, "y": 2.6, "z": 1.5 },
        { "x": 2, "y": 3, "z": 1.5 }
    ],
    [
        { "x": 3, "y": -0.33333333333333337, "z": 1.5 },
        { "x": 3, "y": -0.33333333333333337, "z": 2 },
        { "x": 3, "y": 2.6, "z": 1.5 }
    ],
    [
        { "x": 3, "y": -0.33333333333333337, "z": 2 },
        { "x": 3, "y": 2.6, "z": 2 },
        { "x": 3, "y": 2.6, "z": 1.5 }
    ],
    [
        { "x": 3, "y": -0.33333333333333337, "z": 2 },
        { "x": 6, "y": 0.6666666666666667, "z": 2 },
        { "x": 3, "y": 2.6, "z": 2 }
    ],
    [
        { "x": 6, "y": 0.6666666666666667, "z": 2 },
        { "x": 6, "y": 1.4, "z": 2 },
        { "x": 3, "y": 2.6, "z": 2 }
    ],
    [
        { "x": 6, "y": 0.6666666666666667, "z": 2 },
        { "x": 7, "y": 1, "z": 2.3333333333333335 },
        { "x": 6, "y": 1.4, "z": 2 }
    ],
    [
        { "x": 7, "y": 1, "z": 4.5 },
        { "x": 4, "y": 0, "z": 4.5 },
        { "x": 4, "y": 2.2, "z": 4.5 }
    ],
    [
        { "x": 4, "y": 0, "z": 4.5 },
        { "x": 2, "y": -0.6666666666666667, "z": 4.25 },
        { "x": 4, "y": 2.2, "z": 4.5 }
    ],
    [
        { "x": 2, "y": -0.6666666666666667, "z": 4.25 },
        { "x": 2, "y": 3, "z": 4.25 },
        { "x": 4, "y": 2.2, "z": 4.5 }
    ],
    [
        { "x": 2, "y": -0.6666666666666667, "z": 4.25 },
        { "x": 1, "y": -1, "z": 4.125 },
        { "x": 2, "y": 3, "z": 4.25 }
    ]
]
'''

# Load the JSON data
triangles_data = json.loads(triangles_json)

# Extract the vertices of the triangles
triangles = [[(point['x'], point['y'], point['z']) for point in triangle] for triangle in triangles_data]

# Calculate the limits for the axes
x_values = [point['x'] for triangle in triangles_data for point in triangle]
y_values = [point['y'] for triangle in triangles_data for point in triangle]
z_values = [point['z'] for triangle in triangles_data for point in triangle]

x_min, x_max = min(x_values), max(x_values)
y_min, y_max = min(y_values), max(y_values)
z_min, z_max = min(z_values), max(z_values)

# Create the figure and the 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a collection of 3D polygons (triangles)
mesh = Poly3DCollection(triangles, alpha=0.5, edgecolor='r')

# Add the mesh to the axis
ax.add_collection3d(mesh)

# Set axis limits dynamically
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.set_zlim([z_min, z_max])

# Set axis labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Display the mesh
plt.show()

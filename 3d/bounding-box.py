import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import numpy as np

# Coordinate dei due punti
# CO12 H120 speaker
# p1 = {"x": -0.42359399795532227, "y": -0.5715000033378601, "z": -0.1777999997138977}
# p2 = {"x": 0.13600000739097595, "y": 0.5715000033378601, "z": 0.1777999997138977}

# CP218 II+ speaker
# p1 = {"x": -0.8064500093460083, "y": -0.6044999957084656, "z": 0}
# p2 = {"x": 0, "y": 0.6044999957084656, "z": 0.5647732019424438}

# Slider bounding box
bbox_values = [
    {"x": -1.0794999599456787, "y": -0.027384374290704727, "z": -0.15240000188350677},
    {"x": 0.03, "y": 0.027384374290704727, "z": 0.03},
]

# Grid bounding box
# bbox_values = [
#     {
#         "x": -0.5512422323226929,
#         "y": -0.5715000033378601,
#         "z": -0.15240000188350677,
#     },
#     {
#         "x": 0.039307769387960434,
#         "y": 0.5715000033378601,
#         "z": 0.038100000470876694,
#     },
# ]

# Extract and round points
p1 = {k: round(v, 2) for k, v in bbox_values[0].items()}
p2 = {k: round(v, 2) for k, v in bbox_values[1].items()}

# Vertices and edges of the bounding box
x_min, y_min, z_min = p1["x"], p1["y"], p1["z"]
x_max, y_max, z_max = p2["x"], p2["y"], p2["z"]
vertices = [
    [x_min, y_min, z_min], [x_max, y_min, z_min],
    [x_max, y_max, z_min], [x_min, y_max, z_min],
    [x_min, y_min, z_max], [x_max, y_min, z_max],
    [x_max, y_max, z_max], [x_min, y_max, z_max],
]
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]

# Function to plot bounding box and axes


def plot_bounding_box(ax, view=None):
    lines = [[vertices[start], vertices[end]] for start, end in edges]
    lc = Line3DCollection(lines, colors="blue", linewidths=1.5)
    ax.add_collection3d(lc)

    origin = [0, 0, 0]
    ax.quiver(*origin, 0.2, 0, 0, color="red", linewidth=2)  # X-axis
    ax.quiver(*origin, 0, 0.2, 0, color="green", linewidth=2)  # Y-axis
    ax.quiver(*origin, 0, 0, 0.2, color="blue", linewidth=2)  # Z-axis

    # Set the same scale for all axes
    max_range = max(x_max - x_min, y_max - y_min, z_max - z_min)
    ax.set_xlim((x_min + x_max) / 2 - max_range / 2,
                (x_min + x_max) / 2 + max_range / 2)
    ax.set_ylim((y_min + y_max) / 2 - max_range / 2,
                (y_min + y_max) / 2 + max_range / 2)
    ax.set_zlim((z_min + z_max) / 2 - max_range / 2,
                (z_min + z_max) / 2 + max_range / 2)

    # Configure view
    if view == 'top':
        ax.view_init(elev=90, azim=-90)  # Top view (XY)
        ax.zaxis.line.set_lw(0)
        ax.set_zticks([])
        ax.zaxis.label.set_visible(False)
    elif view == 'side':
        ax.view_init(elev=0, azim=0)  # Side view (YZ)
        ax.xaxis.line.set_lw(0)
        ax.set_xticks([])
        ax.xaxis.label.set_visible(False)
    elif view == 'xz':
        ax.view_init(elev=0, azim=-90)  # Plane view (XZ)
        ax.yaxis.line.set_lw(0)
        ax.set_yticks([])
        ax.yaxis.label.set_visible(False)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")


# Create the figure and subplots
fig = plt.figure(figsize=(12, 16))

# Row 1: Text for bounding box values
text_ax = fig.add_subplot(311)
text_ax.axis("off")
rounded_p1 = {k: round(v, 2) for k, v in p1.items()}
rounded_p2 = {k: round(v, 2) for k, v in p2.items()}
text = f"Bounding Box Points:\nPoint 1: {rounded_p1}\nPoint 2: {rounded_p2}"
text_ax.text(0.5, 0.5, text, ha="center", va="center",
             fontsize=12, transform=text_ax.transAxes)

# Row 2: 3D View (Orthographic) and Top View (XY)
ax1 = fig.add_subplot(323, projection="3d")
ax1.set_proj_type('ortho')
plot_bounding_box(ax1)
ax1.set_title("3D View (Orthographic)")

ax2 = fig.add_subplot(324, projection="3d")
ax2.set_proj_type('ortho')
plot_bounding_box(ax2, view='top')
ax2.set_title("Top View (XY)")

# Row 3: Side View (YZ) and Plane View (XZ)
ax3 = fig.add_subplot(325, projection="3d")
ax3.set_proj_type('ortho')
plot_bounding_box(ax3, view='side')
ax3.set_title("Side View (YZ)")

ax4 = fig.add_subplot(326, projection="3d")
ax4.set_proj_type('ortho')
plot_bounding_box(ax4, view='xz')
ax4.set_title("Plane View (XZ)")

# Adjust layout for readability
plt.tight_layout()
plt.show()

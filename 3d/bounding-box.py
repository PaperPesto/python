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

# Sub Cluster
p1 = {"x": -0.8064500093460083, "y": -0.6044999957084656, "z": 0}
p2 = {"x": 0, "y": 0.6044999957084656, "z": 1.6967732019424435}



# Arrotondiamo i punti a 2 decimali
p1_rounded = {k: round(v, 2) for k, v in p1.items()}
p2_rounded = {k: round(v, 2) for k, v in p2.items()}

# Calcolo dei vertici della bounding box
x_min, y_min, z_min = p1["x"], p1["y"], p1["z"]
x_max, y_max, z_max = p2["x"], p2["y"], p2["z"]

vertices = [
    [x_min, y_min, z_min],
    [x_max, y_min, z_min],
    [x_max, y_max, z_min],
    [x_min, y_max, z_min],
    [x_min, y_min, z_max],
    [x_max, y_min, z_max],
    [x_max, y_max, z_max],
    [x_min, y_max, z_max],
]

# Definiamo gli spigoli della bounding box
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # base inferiore
    (4, 5), (5, 6), (6, 7), (7, 4),  # base superiore
    (0, 4), (1, 5), (2, 6), (3, 7),  # verticali
]

# Funzione per disegnare la bounding box e gli assi
def plot_bounding_box(ax, view=None):
    # Disegniamo gli spigoli
    lines = [[vertices[start], vertices[end]] for start, end in edges]
    lc = Line3DCollection(lines, colors="blue", linewidths=1.5)
    ax.add_collection3d(lc)

    # Disegniamo l'origine con i vettori (lunghezza 0.2)
    origin = [0, 0, 0]
    ax.quiver(*origin, 0.2, 0, 0, color="red", linewidth=2)  # X rosso
    ax.quiver(*origin, 0, 0.2, 0, color="green", linewidth=2)  # Y verde
    ax.quiver(*origin, 0, 0, 0.2, color="blue", linewidth=2)  # Z blu

    # Calcoliamo il range per gli assi
    ranges = np.array([
        [x_min, x_max],
        [y_min, y_max],
        [z_min, z_max]
    ])
    axis_limits = [
        ranges[:, 0].min(), ranges[:, 1].max()
    ]
    max_range = axis_limits[1] - axis_limits[0]
    mid_x = (x_min + x_max) / 2
    mid_y = (y_min + y_max) / 2
    mid_z = (z_min + z_max) / 2

    # Impostiamo la stessa scala per tutti gli assi
    ax.set_xlim(mid_x - max_range / 2, mid_x + max_range / 2)
    ax.set_ylim(mid_y - max_range / 2, mid_y + max_range / 2)
    ax.set_zlim(mid_z - max_range / 2, mid_z + max_range / 2)

    # Configuriamo la vista
    if view == 'top':
        ax.view_init(elev=90, azim=-90)  # Vista dall'alto (XY)
        
        # Nascondo l'asse z
        ax.zaxis.line.set_lw(0)  # Nasconde la linea dell'asse Z
        ax.set_zticks([])  # Rimuove i tick dell'asse Z
        ax.zaxis.label.set_visible(False)  # Nasconde l'etichetta dell'asse Z
    elif view == 'side':
        ax.view_init(elev=0, azim=0)  # Vista laterale (XZ)
        
        # Nascondo l'asse x
        ax.xaxis.line.set_lw(0)  # Nasconde la linea dell'asse X
        ax.set_xticks([])  # Rimuove i tick dell'asse X
        ax.xaxis.label.set_visible(False)  # Nasconde l'etichetta dell'asse X

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

# Creazione della figura con un layout esteso
fig = plt.figure(figsize=(12, 10))

# Subplot per visualizzare i punti della bounding box
text_ax = fig.add_subplot(211)
text_ax.axis("off")  # Nascondiamo gli assi
text = f"Bounding Box Points:\n" \
       f"Point 1: {p1_rounded}\n" \
       f"Point 2: {p2_rounded}"
text_ax.text(0.5, 0.5, text, ha="center", va="center", fontsize=12, transform=text_ax.transAxes)

# Tre subplot per le viste 3D
axes = [fig.add_subplot(234 + i, projection="3d") for i in range(3)]

# Vista 3D con proiezione ortografica
axes[0].set_proj_type('ortho')
plot_bounding_box(axes[0])
axes[0].set_title("Vista 3D (Ortografica)")

# Vista ortogonale dall'alto (XY)
axes[1].set_proj_type('ortho')
plot_bounding_box(axes[1], view='top')
axes[1].set_title("Vista dall'alto (XY)")

# Vista ortogonale laterale (XZ)
axes[2].set_proj_type('ortho')
plot_bounding_box(axes[2], view='side')
axes[2].set_title("Vista laterale (XZ)")

# Ottimizzazione layout
plt.tight_layout(h_pad=2)
plt.show()

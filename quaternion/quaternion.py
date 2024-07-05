import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Funzione per l'interpolazione lineare (LERP)
def lerp(q0, q1, t):
    q = (1 - t) * np.array(q0) + t * np.array(q1)
    q = q / np.linalg.norm(q)  # Normalizzazione per mantenere la proprietà unitaria
    return q

# Funzione per convertire un quaternione in una matrice di rotazione
def quaternion_to_rotation_matrix(q):
    w, x, y, z = q
    return np.array([
        [1 - 2*(y**2 + z**2), 2*(x*y - z*w), 2*(x*z + y*w)],
        [2*(x*y + z*w), 1 - 2*(x**2 + z**2), 2*(y*z - x*w)],
        [2*(x*z - y*w), 2*(y*z + x*w), 1 - 2*(x**2 + y**2)]
    ])

# Crea un cubo unitario
def create_cube():
    r = [-0.5, 0.5]
    vertices = np.array([[x, y, z] for x in r for y in r for z in r])
    return vertices

# Ruota il cubo usando la matrice di rotazione
def rotate_cube(vertices, rotation_matrix):
    return np.dot(vertices, rotation_matrix.T)

# Disegna il cubo
def draw_cube(ax, vertices, color='b'):
    ax.clear()
    ax.scatter3D(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    edges = [
        (0, 1), (0, 2), (0, 4),
        (1, 3), (1, 5), (2, 3),
        (2, 6), (3, 7), (4, 5),
        (4, 6), (5, 7), (6, 7)
    ]
    for edge in edges:
        ax.plot3D(*zip(vertices[edge[0]], vertices[edge[1]]), color=color)
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

# Quaternioni iniziale e finale
q0 = [1, 0, 0, 0]  # Nessuna rotazione
q1 = [0, 1, 0, 0]  # Rotazione di 180 gradi attorno all'asse x

# Crea la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cube_vertices = create_cube()

def update(frame):
    t = frame / (frames - 1)
    q = lerp(q0, q1, t)
    rotation_matrix = quaternion_to_rotation_matrix(q)
    rotated_vertices = rotate_cube(cube_vertices, rotation_matrix)
    draw_cube(ax, rotated_vertices)

frames = 50
ani = animation.FuncAnimation(fig, update, frames=frames, interval=100)

video_path = "./lerp_quaternion_interpolation.mp4"
ani.save(video_path, writer='ffmpeg')

video_path

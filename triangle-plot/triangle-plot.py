import matplotlib.pyplot as plt
import json

# Example JSON data for the triangle
triangle_json = '''
[
    { "x": 1, "y": -1 },
    { "x": 7, "y": 1 },
    { "x": 2, "y": 3 },
    { "x": 1, "y": -1 }
]
'''

# Example JSON data for the line
line_json = '''
[
    { "x": -3, "z": 1 },
    { "x": -2, "z": 1 },
    { "x": 2, "z": 1.5 },
    { "x": 3, "z": 1.5 },
    { "x": 3, "z": 2 },
    { "x": 6, "z": 2 },
    { "x": 9, "z": 3 },
    { "x": 8, "z": 4 },
    { "x": 7, "z": 4.5 },
    { "x": 4, "z": 4.5 },
    { "x": 0, "z": 4 }
]
'''

# Load the JSON data
triangle_data = json.loads(triangle_json)
line_data = json.loads(line_json)

# Extract the coordinates of the triangle
triangle_x = [point['x'] for point in triangle_data]
triangle_y = [point['y'] for point in triangle_data]

# Extract the coordinates of the line
line_x = [point['x'] for point in line_data]
line_z = [point['z'] for point in line_data]

# Create the figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

# Set the same limits on the x axes
min_x = min(min(triangle_x), min(line_x))
max_x = max(max(triangle_x), max(line_x))

# Draw the triangle on the x-y plot
ax1.plot(triangle_x, triangle_y, marker='o', linestyle='-', color='b')
ax1.set_title('Triangle in the x-y plane')
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_xlim(min_x, max_x)
ax1.grid(True)

# Draw the line on the x-z plot
ax2.plot(line_x, line_z, marker='o', linestyle='-', color='r')
ax2.set_title('Line in the x-z plane')
ax2.set_xlabel('x axis')
ax2.set_ylabel('z axis')
ax2.set_xlim(min_x, max_x)
ax2.grid(True)

# Save the image
plt.tight_layout()
plt.savefig('charts.png')

# Show the plots
# plt.show()

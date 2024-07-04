import matplotlib.pyplot as plt
import json

# Example JSON data for the triangle
triangle_json = '''
[
    { "x": 1, "y": -1 },
     { "x": 2, "y": -0.666 },
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
      { "x": 1, "z": 1.375 },
      { "x": 2, "z": 1.5 },
      { "x": 3, "z": 1.5 },
      { "x": 3, "z": 2 },
      { "x": 6, "z": 2 },
      { "x": 7, "z": 2.3333333333333335 },
      { "x": 9, "z": 3 },
      { "x": 8, "z": 4 },
      { "x": 7, "z": 4.5 },
      { "x": 4, "z": 4.5 },
      { "x": 2, "z": 4.25 },
      { "x": 1, "z": 4.125 },
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

# Define the segments to be added (to show the triangle generated)
segments = [
    # {"x1": 1, "y1": -1, "x2": 2, "y2": 3},
    {"x1": 2, "y1": -0.666, "x2": 2, "y2": 3},
    {"x1": 3, "y1": -0.333, "x2": 2, "y2": 3},
    {"x1": 3, "y1": -0.333, "x2": 3, "y2": 2.6}
]

# Define texts to be added
texts = [
    {"x": 2.2, "z": 0.3, "text": "T0"},
    {"x": 2.6, "z": 1.7, "text": "T1"},
    {"x": 2, "z": -0.66, "text": "0"},
    {"x": 3, "z": -0.33, "text": "1"},
    {"x": 2, "z": 3, "text": "2"},
    {"x": 3, "z": 2.66, "text": "3"}
]
offset = 0.05

# Create the figure and axes
fig, (ax1) = plt.subplots(1, 1, figsize=(8, 8))

# Set the same limits on the x axes
min_x = min(min(triangle_x), min(line_x))
max_x = max(max(triangle_x), max(line_x))

# Draw the triangle on the x-y plot
ax1.plot(triangle_x, triangle_y, marker='o', linestyle='-', color='b')
ax1.set_title('Triangle in the x-y plane')
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
# ax1.set_xlim(min_x, max_x)
ax1.set_ylim(min_x, max_x)
ax1.grid(True)

# Add the segments to the x-y plot
for segment in segments:
    ax1.plot([segment['x1'], segment['x2']], [segment['y1'], segment['y2']], 'k--')
    
# Add text "T" at the point (1.5, 1.5)
for text in texts:
    ax1.text(text["x"] + offset, text["z"] + offset, text["text"], fontsize=12, color='black')



# Draw the line on the x-z plot
# ax2.plot(line_x, line_z, marker='o', linestyle='-', color='r')
# ax2.set_title('Line in the x-z plane')
# ax2.set_xlabel('x axis')
# ax2.set_ylabel('z axis')
# ax2.set_xlim(min_x, max_x)
# ax2.grid(True)

# Add dashed lines corresponding to the x-coordinates of the triangle
# for x in triangle_x:
#     ax2.axvline(x=x, color='b', linestyle='--')
    
# Add dashed lines corresponding to the x-coordinates of the section
# for x in line_x:
#     ax1.axvline(x=x, color='r', linestyle='--')

# Save the image
plt.tight_layout()
plt.savefig('mesh-extrusion-algorithm-4-intersections-triangle.png')

# Show the plots
plt.show()

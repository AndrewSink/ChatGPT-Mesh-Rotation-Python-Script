import trimesh
import numpy as np
import random

# Load the STL file
mesh = trimesh.load("input.stl")

for i in range(3):
    # Generate a random angle between 0 and 360 degrees
    angle = random.uniform(0, 360)

    # Convert the angle to radians
    angle_rad = np.deg2rad(angle)

    # Define the rotation matrices on the X, Y, and Z axes
    rotation_matrix_x = np.array([
        [1, 0, 0],
        [0, np.cos(angle_rad), -np.sin(angle_rad)],
        [0, np.sin(angle_rad), np.cos(angle_rad)]
    ])

    rotation_matrix_y = np.array([
        [np.cos(angle_rad), 0, np.sin(angle_rad)],
        [0, 1, 0],
        [-np.sin(angle_rad), 0, np.cos(angle_rad)]
    ])

    rotation_matrix_z = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad), 0],
        [np.sin(angle_rad), np.cos(angle_rad), 0],
        [0, 0, 1]
    ])

    # Extend the rotation matrices to 4x4 transformation matrices
    rotation_matrix_x_4x4 = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle_rad), -np.sin(angle_rad), 0],
        [0, np.sin(angle_rad), np.cos(angle_rad), 0],
        [0, 0, 0, 1]
    ])

    rotation_matrix_y_4x4 = np.array([
        [np.cos(angle_rad), 0, np.sin(angle_rad), 0],
        [0, 1, 0, 0],
        [-np.sin(angle_rad), 0, np.cos(angle_rad), 0],
        [0, 0, 0, 1]
    ])

    rotation_matrix_z_4x4 = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad), 0, 0],
        [np.sin(angle_rad), np.cos(angle_rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    # Apply the rotations to the mesh
    mesh.apply_transform(rotation_matrix_x_4x4)
    mesh.apply_transform(rotation_matrix_y_4x4)
    mesh.apply_transform(rotation_matrix_z_4x4)

    # Save the rotated mesh to an STL file
    mesh.export("output_{}.stl".format(i+1))

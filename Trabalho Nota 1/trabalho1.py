
import numpy as np
import math
import matplotlib.pyplot as plt

# Define the window and viewport limits
window_limits = {
    'xmin': -1,
    'ymin': -1,
    'xmax': 1,
    'ymax': 1
}

viewport_limits = {
    'xmin': 0,
    'ymin': 0,
    'xmax': 500,
    'ymax': 500
}

# Initialize transformation matrices
transformation_matrices = {
    'translation': np.eye(4),
    'rotation_x': np.eye(4),
    'rotation_y': np.eye(4),
    'rotation_z': np.eye(4),
    'scale': np.eye(4)
}

# Initialize camera transformation matrices
camera_matrices = {
    'translation': np.array([[1, 0, 0, 0],
                             [0, 1, 0, 0],
                             [0, 0, 1, -10],
                             [0, 0, 0, 1]]),
    'rotation_x': np.eye(4),
    'rotation_y': np.eye(4),
    'rotation_z': np.eye(4)
}

# Initialize projection matrix
fovy = math.radians(67.0)
aspect = 1.0
zNear = 0.1
zFar = 100

a = 1 / (math.tan(fovy / 2) * aspect)
b = 1 / (math.tan(fovy / 2))
c = (zFar + zNear) / (zNear - zFar)
d = (2 * zFar * zNear) / (zNear - zFar)

projection_matrix = np.array([
    [a, 0, 0, 0],
    [0, b, 0, 0],
    [0, 0, c, d],
    [0, 0, -1, 0]
])

# Define model coordinates
model_coordinates = [
    [0.000000, -1.000000, -1.000000, 1.0],
    [0.195090, -1.000000, -0.980785, 1.0],
    # ... Add the rest of the coordinates here
    [0.000000, 1.000000, 0.000000, 1.0]
]

# Define a function to perform mapping
def map_coordinates(p):
    plt.xlim(viewport_limits['xmin'], viewport_limits['xmax'])
    plt.ylim(viewport_limits['ymin'], viewport_limits['ymax'])

    xvp = ((p[0] - window_limits['xmin']) * (viewport_limits['xmax'] - viewport_limits['xmin'])) / (window_limits['xmax'] - window_limits['xmin']) + viewport_limits['xmin']
    yvp = ((p[1] - window_limits['ymin']) * (viewport_limits['ymax'] - viewport_limits['ymin'])) / (window_limits['ymax'] - window_limits['ymin']) + viewport_limits['ymin']

    plt.scatter(xvp, yvp)

# Define a function to display points
def display_points(points):
    for point in points:
        print(point)

print('\nAplicação que implementa um pipeline de visualização 3D completo\n')

while True:
    print("1. Manipular o objeto")
    print("2. Manipular a Câmera")
    print("3. Modificar projeção")
    print("4. Modificar mapeamento:")
    print("5. Visualizar objeto:")
    print("6. Calculos:")
    print("9. Sair:")

    option = int(input("Digite a opção: "))

    if option == 1:
        print("1. Translação")
        print("2. Escala")
        print("3. Rotação em X")
        print("4. Rotação em Y:")
        print("5. Rotação em Z:")

        operation = int(input("Digite a opção: "))

        if operation == 1:
            tx = float(input("Digite o valor de tx: "))
            ty = float(input("Digite o valor de ty: "))
            tz = float(input("Digite o valor de tz: "))
            transformation_matrices['translation'] = np.array([
                [1, 0, 0, tx],
                [0, 1, 0, ty],
                [0, 0, 1, tz],
                [0, 0, 0, 1]
            ])
        # ... Add handling for other transformations (scale, rotation)

    elif option == 2:
        print("1. Translação")
        print("2. Rotação em X")
        print("3. Rotação em Y:")
        print("4. Rotação em Z:")

        operation = int(input("Digite a opção: "))

        if operation == 1:
            txCam = float(input("Digite o valor de txCam: "))
            tyCam = float(input("Digite o valor de tyCam: "))
            tzCam = float(input("Digite o valor de tzCam: "))

            camera_matrices['translation'] = np.array([
                [1, 0, 0, -txCam],
                [0, 1, 0, -tyCam],
                [0, 0, 1, -tzCam],
                [0, 0, 0, 1]
            ])
        # ... Add handling for other camera transformations

    elif option == 3:
        print("1. Projeção perspectiva")
        print("2. Projeção paralela")

        operation = int(input("Digite a opção: "))

        if operation == 1:
            # Update the projection matrix for perspective projection
            fovy = math.radians(67.0)
            aspect = 1.0
            zNear = 0.1
            zFar = 100

            a = 1 / (math.tan(fovy / 2) * aspect)
            b = 1 / (math.tan(fovy / 2))
            c = (zFar + zNear) / (zNear - zFar)
            d = (2 * (zFar * zNear)) / (zNear - zFar)

            projection_matrix = np.array([
                [a, 0, 0, 0],
                [0, b, 0, 0],
                [0, 0, c, d],
                [0, 0, -1, 0]
            ])
        # ... Add handling for other projection types

    elif option == 4:
        print("1. Window")
        print("2. Viewport")

        operation = int(input("Digite a opção: "))

        if operation == 1:
            window_limits['xmin'] = int(input("Valor do xminw: "))
            window_limits['xmax'] = int(input("Valor do xmaxw: "))
            window_limits['ymin'] = int(input("Valor do yminw: "))
            window_limits['ymax'] = int(input("Valor do ymaxw: "))
        elif operation == 2:
            viewport_limits['xmin'] = int(input("Valor do xminvp: "))
            viewport_limits['xmax'] = int(input("Valor do xmaxvp: "))
            viewport_limits['ymin'] = int(input("Valor do yminvp: "))
            viewport_limits['ymax'] = int(input("Valor do ymaxvp: "))
        else:
            print("Opção inválida!")

    elif option == 5:
        # Transform the model coordinates using the matrices
        transformed_points = []
        for coord in model_coordinates:
            # Apply the transformations in the order: translation -> rotation -> scale
            transformed_coord = np.dot(transformation_matrices['translation'], coord)
            transformed_coord = np.dot(transformation_matrices['rotation_x'], transformed_coord)
            transformed_coord = np.dot(transformation_matrices['rotation_y'], transformed_coord)
            transformed_coord = np.dot(transformation_matrices['rotation_z'], transformed_coord)
            transformed_coord = np.dot(transformation_matrices['scale'], transformed_coord)
            transformed_points.append(transformed_coord)

        # Perform perspective projection
        projected_points = []
        for coord in transformed_points:
            homo_coord = np.dot(projection_matrix, coord)
            if homo_coord[3] != 0:
                projected_coord = homo_coord[:3] / homo_coord[3]
                projected_points.append(projected_coord)

        # Map the projected points to the viewport and display them
        plt.clf()
        for coord in projected_points:
            map_coordinates(coord)
        plt.show()

    elif option == 6:
        # Calculate the transformed points
        transformed_points = []
        for coord in model_coordinates:
            # Apply the transformations in the order: translation -> rotation -> scale
            transformed_coord = np.dot(transformation_matrices['translation'], coord)
            transformed_coord = np.dot(transformation_matrices['rotation_x'], transformed_coord)
            transformed_coord = np.dot(transformation_matrices['rotation_y'], transformed_coord)
            transformed_coord = np.dot(transformation_matrices['rotation_z'], transformed_coord)
            transformed_coord = np.dot(transformation_matrices['scale'], transformed_coord)
            transformed_points.append(transformed_coord)

        # Calculate the perspective projection
        projected_points = []
        for coord in transformed_points:
            homo_coord = np.dot(projection_matrix, coord)
            if homo_coord[3] != 0:
                projected_coord = homo_coord[:3] / homo_coord[3]
                projected_points.append(projected_coord)

        print("\nCoordenadas do objeto após as transformações:")
        display_points(transformed_points)
        print("\nCoordenadas do objeto após a projeção:")
        display_points(projected_points)

    elif option == 9:
        break

    else:
        print("Opção inválida!")

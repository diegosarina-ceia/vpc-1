import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_video_quality_measure(quality_measures: list) -> None:
    """
    Grafica la Medida de Calidad de Imagen (FM) de cada frame en un video.

    args:
        quality_measures (list): List of Image Quality Measures (FM) for each frame in the video.
    """
    plt.plot(quality_measures)
    plt.xlabel('Frame')
    plt.ylabel('Image Quality Measure (FM)')
    plt.title('Image Quality Measure (FM) for each frame in the video')
    plt.show()

def draw_image_detection_none(image: np.ndarray, *args) -> np.ndarray:
    return image

def draw_image_detection_roi(image: np.ndarray, shape_image: tuple, color: tuple, roi_percentage: float) -> np.ndarray:
    """
    Dibuja un círculo en el centro de la imagen.

    args:
        image (np.ndarray): Input image.
        color (tuple): Color of the circle.
        **kwargs: Arbitrary keyword arguments.
    
    return:
        np.ndarray: Output image with the circle drawn.
    """
    roi_height = int(shape_image[1] * roi_percentage)
    roi_width = int(shape_image[0] * roi_percentage)
    y1 = shape_image[1] // 2 - roi_height // 2
    y2 = y1 + roi_height
    x1 = shape_image[0] // 2 - roi_width // 2
    x2 = x1 + roi_width
    
    cv.rectangle(image, (x1, y1), (x2, y2), color, 2)

    return image

def draw_image_detection_matrix(image: np.ndarray, shape_image: tuple, color: tuple, grid_size: tuple, scale_factor:float=1.0, offset:int=2) -> np.ndarray:
    """
    Dibuja una matriz de círculos en la imagen.

    args:
        image (np.ndarray): Input image.
        shape_image (tuple): Shape of the input image.
        color (tuple): Color of the circle.
        grid_size (tuple): Number of rows and columns in the grid.
        scale_factor (float): Scale factor to resize the circles.
    
    return:
        np.ndarray: Output image with the circle drawn.
    """
    # Calcular el tamaño ajustado de la grilla basado en el factor de escala
    scaled_height = int(shape_image[1] * scale_factor)
    scaled_width = int(shape_image[0] * scale_factor)

    rows, cols = grid_size
    step_y = scaled_height // rows
    step_x = scaled_width // cols

    center_y = shape_image[1] // 2
    center_x = shape_image[0] // 2
    
    start_y = center_y - (scaled_height // 2)
    start_x = center_x - (scaled_width // 2)

    # Añadir los valores de la matriz de enfoque como texto en cada subregión
    for i in range(rows):
        for j in range(cols):
            y1 = start_y + i * step_y + offset
            y2 = y1 + step_y - offset
            x1 = start_x + j * step_x + offset
            x2 = x1 + step_x - offset
            
            cv.rectangle(image, (x1, y1), (x2, y2), color, 2)           

    return image
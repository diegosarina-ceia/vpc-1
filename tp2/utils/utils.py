import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from typing import Tuple, List
GridSize = Tuple[int, int]

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

def draw_image_detection_roi(image: np.ndarray, color: tuple, roi_percentage: float) -> np.ndarray:
    """
    Dibuja un círculo en el centro de la imagen.

    args:
        image (np.ndarray): Input image.
        color (tuple): Color of the circle.
        **kwargs: Arbitrary keyword arguments.
    
    return:
        np.ndarray: Output image with the circle drawn.
    """

    shape_image = image.shape

    # para asegurar el porcenteje del area de la imagen
    roi_percentage = np.sqrt(roi_percentage)

    roi_height = int(shape_image[0] * roi_percentage)
    roi_width = int(shape_image[1] * roi_percentage)
    y1 = shape_image[0] // 2 - roi_height // 2
    y2 = y1 + roi_height
    x1 = shape_image[1] // 2 - roi_width // 2
    x2 = x1 + roi_width
    
    cv.rectangle(image, (x1, y1), (x2, y2), color, 2)

    return image

def draw_image_detection_matrix(image: np.ndarray, color: tuple=(255,0,0), grid_size: tuple=(4,4), scale_factor:float=1.0, offset:int=2) -> np.ndarray:
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

    shape_image = image.shape

    # Calcular el tamaño ajustado de la grilla basado en el factor de escala
    scaled_height = int(shape_image[0] * scale_factor)
    scaled_width = int(shape_image[1] * scale_factor)

    rows, cols = grid_size
    step_y = scaled_height // rows
    step_x = scaled_width // cols

    center_y = shape_image[0] // 2
    center_x = shape_image[1] // 2
    
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

def show_imgs(imgs, size=(10, 6), title='', funtion_draw=draw_image_detection_none, **kwargs):
    """
    Muestra una lista de imágenes en una sola fila.

    args:
        imgs (list): Lista de rutas de las imágenes a mostrar.
        size (tuple): Tamaño de la figura.
        title (str): Título de la figura.
    """
    num_imgs = len(imgs)
    rows = num_imgs
    cols = 1  # Siempre una sola columna

    plt.figure(figsize=(size[0], size[1] * rows))
    for i, img in enumerate(imgs):
        plt.subplot(rows, cols, i + 1)
        img_data = cv.cvtColor(funtion_draw(cv.imread(img),**kwargs), cv.COLOR_BGR2RGB)
        plt.imshow(img_data)
        plt.title(f"{title} {i+1}" if title else '')
        plt.axis('off')
    plt.tight_layout()
    plt.show()

def plot_focus_matrix_on_image(image:np.ndarray, fm_matrix: List[float], grid_size: GridSize, scale_factor:float=1.0)-> None:
    """
    Plotea la matriz de enfoque en la imagen de entrada, dividiendo la imagen en una grilla de sub-imágenes basado
    en el parametro grid_size y el factor de escala scale_factor.

    Args:
        image (np.ndarray): Imagen de entrada, representada como un array 2D de NumPy.
        grid_size (GridSize): Tamaño de la grilla para dividir la imagen (filas, columnas).
        scale_factor (float): Factor de escala para ajustar el tamaño de la grilla. Default es 1.0.
    """
    height, width = image.shape
    
    # Calcular el tamaño ajustado de la grilla basado en el factor de escala
    scaled_height = int(height * scale_factor)
    scaled_width = int(width * scale_factor)
    
    rows, cols = grid_size
    step_y = scaled_height // rows
    step_x = scaled_width // cols
    
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(image, cmap='gray')

    center_y = height // 2
    center_x = width // 2
    
    start_y = center_y - (scaled_height // 2)
    start_x = center_x - (scaled_width // 2)

    # Añadir los valores de la matriz de enfoque como texto en cada subregión
    for i in range(rows):
        for j in range(cols):
            y1 = start_y + i * step_y
            y2 = y1 + step_y
            x1 = start_x + j * step_x
            x2 = x1 + step_x
            
            fm_value = fm_matrix[i * cols + j]
            
            # Dibujar el rectángulo
            rect = plt.Rectangle((x1, y1), step_x, step_y, edgecolor='green', facecolor='none', linewidth=1)
            ax.add_patch(rect)
            
            # Añadir el valor del FM en el centro del rectángulo
            ax.text(x1 + step_x / 2, y1 + step_y / 2, f'{fm_value:.2f}', color='yellow', ha='center', va='center', fontsize=6, bbox=dict(facecolor='black', alpha=0.5))

    ax.set_title(f'Matriz de enfoque con dimensiones {rows}x{cols} en imagen')
    plt.show()
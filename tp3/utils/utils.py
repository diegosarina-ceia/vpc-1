import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

from typing import List

def show_images(image_paths: List[str]) -> None:
    """
    Muestra las imágenes en una grilla de 3 columnas.

    Args:
        image_paths (List[str]): Lista de rutas de las imágenes a mostrar.
    """
    num_images = len(image_paths)
    num_cols = 3
    num_rows = (num_images + num_cols - 1) // num_cols
    
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))
    
    for i, img_path in enumerate(image_paths):
        img = cv.imread(img_path)
        if img is not None and not img.size == 0:
            imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            height, width = img.shape[:2]
            title = f'{img_path}\n{width}x{height}'
            axs[i // num_cols, i % num_cols].imshow(imgRGB)
            axs[i // num_cols, i % num_cols].set_title(title)
            axs[i // num_cols, i % num_cols].axis('off')
        else:
            print(f"Error: {img_path} está vacía o cargada incorrectamente.")
    
    # Ocultar ejes no utilizados
    for j in range(i + 1, num_rows * num_cols):
        fig.delaxes(axs[j // num_cols, j % num_cols])

    plt.tight_layout()
    plt.show()

def graf_boxplot(image: np.ndarray, match: list) -> np.ndarray:
    """
    Grafica de boxplot y valor de métrica

    Args:
        -image: imagen en la que se va a graficar el boxplot y el valor de la métrica.
        -match: lista con los valores de la métrica y la posición de la coincidencia.
    
    Returns:
        -image: imagen con el boxplot y el valor de la métrica.
    """
    
    match_value, match_location, match_shape_temple, match_scale = match
    x, y = int(match_location[0]/match_scale), int(match_location[1]/match_scale)
    h, w = int(match_shape_temple[0]/match_scale), int(match_shape_temple[1]/match_scale)

    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.rectangle(image, (x, y), (x + w, y - 20), (0, 255, 0), -1)
    cv.putText(image, f'{match_value:.2f}', (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.33, (255, 255, 255), 1)

    return image

def graf_multi_boxplot(image: np.ndarray, matches: list) -> np.ndarray:
    """
    Grafica de boxplot y valor de métrica

    Args:
        -image: imagen en la que se va a graficar el boxplot y el valor de la métrica.
        -match: lista con los valores de la métrica y la posición de varias coincidencias.
    
    Returns:
        -image: imagen con el boxplot y el valor de la métrica.
    """
    
    for match in matches:
        image = graf_boxplot(image, match)

    return image

def graf_all_scaled_one_image(resultados: dict, methods_str: List[str], image_path: str) -> None:
    """
    Función que grafica los resultados de la detección de un logo en una imagen a diferentes escalas.

    Args:
        - resultados: diccionario con los resultados de la detección.
        - methods_str: lista de strings con los métodos utilizados.
        - image_path: string con la ruta de la imagen.
    """
    for method in methods_str:
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))

        # Grafico la evolución de la métrica en función de la escala
        axs[0].plot([x[3] for x in resultados[method]], [x[0] for x in resultados[method]])
        axs[0].set_title(f'{method} vs Scale')
        axs[0].set_xlabel('Scale')
        axs[0].set_ylabel(method)
        axs[0].grid(True)

        # Grafico la mejor coincidencia
        if method in ['cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']:
            best_match = min(resultados[method], key=lambda x: x[0])
        else:
            best_match = max(resultados[method], key=lambda x: x[0])

        image = graf_boxplot(cv.imread(image_path), best_match)
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        axs[1].imshow(image)
        axs[1].set_title(f'{method} Best Match')
        axs[1].axis('off') 

        plt.tight_layout()
        plt.show()
    
def remove_overlaps(detecciones: list, overlap_thresh:float=0.2) -> list:
    """
    Función que elimina las detecciones que se superponen utilizando el algoritmo Non-Maximum Suppression.

    Args:
        - detecciones: lista de detecciones.
        - overlap_thresh: umbral de superposición.
        
    Returns:
        - filter_detecciones: lista de detecciones sin superposiciones.
    """
    if len(detecciones) == 0:
        return []

    # elementos que se mantienen
    seleccion = []

    # conversion en boxes
    boxes = [[deteccion[1][0]/deteccion[3],
              deteccion[1][1]/deteccion[3],
              (deteccion[2][1] + deteccion[1][0])/deteccion[3],
              (deteccion[2][0] + deteccion[1][1])/deteccion[3],
              deteccion[3]]/deteccion[3] for deteccion in detecciones]

    boxes = np.array(boxes, dtype="float")

    # Extraer las coordenadas de las cajas
    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,2]
    y2 = boxes[:,3]
    scores = boxes[:,4]

    # Calcular el área de las cajas y ordenar por la coordenada y2 de abajo a arriba
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(scores)

    while len(idxs) > 0:
        # Tomar el índice de la caja con la puntuación más alta
        last = len(idxs) - 1
        i = idxs[last]
        seleccion.append(i)

        # Encontrar las coordenadas de la intersección
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        # Calcular el área de la intersección
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        inter = w * h

        # Calcular la relación de intersección sobre unión (IoU)
        overlap = inter / (area[i] + area[idxs[:last]] - inter)

        # Eliminar todos los índices que tienen un IoU mayor que el umbral
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlap_thresh)[0])))

    # seleccionar solo las detecciones que se mantienen
    detecciones_sin_superposicion = [detecciones[i] for i in seleccion]

    return detecciones_sin_superposicion
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
from threading import Thread

def show_img(img, size=(10,6), title=''):
    plt.figure(figsize=size)
    plt.imshow(cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def show_imgs(imgs, size=(10, 6), title=''):
    num_imgs = len(imgs)
    rows = num_imgs
    cols = 1  # Siempre una sola columna

    plt.figure(figsize=(size[0], size[1] * rows))
    for i, img in enumerate(imgs):
        plt.subplot(rows, cols, i + 1)
        img_data = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB)
        plt.imshow(img_data)
        plt.title(f"{title} {i+1}" if title else '')
        plt.axis('off')
    plt.tight_layout()
    plt.show()

def get_images_from_video(video_path:str, images_path_save:str='enunciado/frames/') -> None:
    capture = cv2.VideoCapture(video_path)
    count = 0

    while (capture.isOpened()):
        ret, frame = capture.read()
        if (ret is True):
            cv2.imwrite(images_path_save + 'IMG_%04d.jpg' % count, frame)
            count += 1
            if (cv2.waitKey(1) == ord('s')):
                break
        else:
            break
    capture.release()
    cv2.destroyAllWindows()


def show_roi_on_image(image, roi_percentage=0.1):
    height, width = image.shape
    roi_height = int(height * roi_percentage)
    roi_width = int(width * roi_percentage)
    
    y1 = height // 2 - roi_height // 2
    y2 = y1 + roi_height
    x1 = width // 2 - roi_width // 2
    x2 = x1 + roi_width
    
    # Dibujar la imagen y el rectángulo del ROI
    plt.figure(figsize=(10, 10))
    plt.imshow(image, cmap='gray')
    plt.gca().add_patch(plt.Rectangle((x1, y1), roi_width, roi_height, edgecolor='red', facecolor='none', linewidth=2))
    plt.title('Image with ROI')
    plt.show()


def show_imgs_with_roi(img_paths, roi_percentage=0.1, size=(10, 6), title=''):
    """
    Muestra una lista de imágenes con una región de interés (ROI) destacada.

    args:
        img_paths (list of str): Lista de rutas a las imágenes.
        roi_percentage (float): Porcentaje del tamaño de la imagen para definir la ROI. Default es 0.1 (10%).
        size (tuple): Tamaño de la figura para cada imagen (ancho, alto). Default es (10, 6).
        title (str): Título base para las imágenes. Default es ''.

    return:
        None
    """
    num_imgs = len(img_paths)
    rows = num_imgs
    cols = 1  # Siempre una sola columna

    plt.figure(figsize=(size[0], size[1] * rows))
    for i, img_path in enumerate(img_paths):
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        height, width = image.shape
        roi_height = int(height * roi_percentage)
        roi_width = int(width * roi_percentage)
        
        y1 = height // 2 - roi_height // 2
        y2 = y1 + roi_height
        x1 = width // 2 - roi_width // 2
        x2 = x1 + roi_width

        plt.subplot(rows, cols, i + 1)
        plt.imshow(image, cmap='gray')
        plt.gca().add_patch(plt.Rectangle((x1, y1), roi_width, roi_height, edgecolor='red', facecolor='none', linewidth=2))
        plt.title(f"{title} {i+1}" if title else '')
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()
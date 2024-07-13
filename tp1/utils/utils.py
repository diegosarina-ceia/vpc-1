import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(path: str) -> np.ndarray:
    """
    Load an image from a given path and change the color space to RGB

    args:
        path: str
            Path to the image
    """
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)


def plot_images(images, titles=None, figsize=(15, 5)) -> None:
    """
    Plot a list of images.

    args:
        images: list of images to visualize
        titles: list of titles to plot. Optional.
        figsize: size of the image. Default (15, 5).
    """
    fig, axs = plt.subplots(1, len(images), figsize=figsize)
    if titles is None:
        titles = [f'Image_{i+1}' for i in range(len(images))]
        
    if len(images) == 1:
        axs = [axs]

    for i, ax in enumerate(axs):
        ax.imshow(images[i])
        ax.set_title(titles[i])
        ax.axis('off')
    
    
    plt.show()
    #return None


def plot_images_comparison(original_images, modified_images, original_titles=None, modified_titles=None, figsize=(15, 5)):
    """
    Plot a list of images to compare

    """
    for i in range(len(original_images)):
        fig, axs = plt.subplots(1, 2, figsize=figsize)
        
        if original_titles is None:
            original_title = f'Original_{i+1}'
        else:
            original_title = original_titles[i]
        
        if modified_titles is None:
            modified_title = f'Chromatic_{i+1}'
        else:
            modified_title = modified_titles[i]
        
        axs[0].imshow(original_images[i])
        axs[0].set_title(original_title)
        axs[0].axis('off')

        axs[1].imshow(modified_images[i])
        axs[1].set_title(modified_title)
        axs[1].axis('off')

        plt.show()

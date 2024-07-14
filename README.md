# CEIA_VisionComputadora1

Trabajo práctico número 1 de la materia Visión Computadora 1 de la Especialización en Inteligencia Artificial de la CEIA.

## Distribución de los archivos

```
├── README.md
├── pyproject.toml
└── tp1
    ├── TP1_VisionComputadora1.ipynb (resulución TP1)
    ├── segmentacion.py (archivo auxiliar)
    ├── enunciado
    │   ├── coord_cromaticas
    │   │   ├── CoordCrom_1.png
    │   │   ├── CoordCrom_2.png
    │   │   └── CoordCrom_3.png
    │   ├── enunciado.png
    │   ├── img1_tp.png
    │   ├── img2_tp.png
    │   ├── segmentacion.png
    │   └── white_patch
    │       ├── test_blue.png
    │       ├── test_green.png
    │       ├── test_red.png
    │       ├── wp_blue.jpg
    │       ├── wp_green.png
    │       ├── wp_green2.jpg
    │       ├── wp_red.png
    │       └── wp_red2.jpg
    └── utils
        ├── __init__.py
        └── utils.py (funciones auxiliares)
```

## Cargar el entorno de trabajo

Para cargar el entorno de trabajo, debe tener una versión de `Python 3.12.x` y ejecutar el siguiente comando en la terminal:

```
pip install poetry (este comando instalara poetry en su version de python elegida)
poetry install (instalara el entorno virtual de este proyecto)
```
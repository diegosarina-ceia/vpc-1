# CEIA_VisionComputadora1

Repositorio con los Trabajos prácticos de la materia Visión Computadora 1 de la Especialización en Inteligencia Artificial de la CEIA.

## Distribución de los archivos

```
├── README.md
├── pyproject.toml
├── tp1
│   ├── TP1_VisionComputadora1.ipynb (resolucion)
│   ├── enunciado
│   │   ├── coord_cromaticas
│   │   │   ├── CoordCrom_1.png
│   │   │   ├── CoordCrom_2.png
│   │   │   └── CoordCrom_3.png
│   │   ├── enunciado.png
│   │   ├── img1_tp.png
│   │   ├── img2_tp.png
│   │   ├── segmentacion.png
│   │   └── white_patch
│   │       ├── test_blue.png
│   │       ├── test_green.png
│   │       ├── test_red.png
│   │       ├── wp_blue.jpg
│   │       ├── wp_green.png
│   │       ├── wp_green2.jpg
│   │       ├── wp_red.png
│   │       └── wp_red2.jpg
│   ├── segmentacion.py
│   └── utils
│       ├── __init__.py
│       └── utils.py (funciones auxiliares)
└── tp2
    ├── TP2_VisionComputadora1.ipynb (resolucion)
    ├── enunciado
    │   ├── focus_video.mov
    │   ├── frames (archivos auxiliares)
    │   │   ├── frame_borroso.jpg
    │   │   ├── frame_medio_borroso_1.jpg
    │   │   ├── frame_medio_borroso_2.jpg
    │   │   └── frame_nitido.jpg
    │   └── proposed_algorithm.png
    ├── output_video (salida de videos)
    │   ├── quality_measure_all_frame.avi
    │   ├── quality_measure_laplacian.avi
    │   ├── quality_measure_matrix_(3, 3).avi
    │   ├── quality_measure_matrix_(4, 4).avi
    │   ├── quality_measure_matrix_(5, 5).avi
    │   ├── quality_measure_matrix_(7, 5).avi
    │   ├── quality_measure_roi.avi
    │   └── unsharp_masking.avi
    ├── papers
    │   ├── AnalysisOfFocusMeasureOperators.pdf
    │   └── ImageSharpnessMeasureforBlurredImagesinFrequency.pdf
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
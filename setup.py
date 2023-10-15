from setuptools import setup

setup(
    name="mxlogging",
    version="1.0.4",
    author="Mario x",
    description=("Un sistema de logging optimizado para una interpretación clara y "
                 "una integración sencilla de mensajes. Pensado para mejorar la trazabilidad "
                 "y el diagnóstico en proyectos de software."),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pistatxos/mxlogging",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['mxlogging', 'mxlogging.utils'],
    python_requires=">=3.7",
)
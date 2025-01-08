from setuptools import setup, find_packages
import os

# Obtén la ruta absoluta del directorio actual
here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='tuproyecto',
    version='0.1',
    description='CrabAge Project',
    author='Andres',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'numpy',
    ]
)
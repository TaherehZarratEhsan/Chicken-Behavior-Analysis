from setuptools import setup, find_packages


setup(
    name='multi-object-tracker',
    author='Aditya M. Deshpande',
    author_email='adityadeshpande2010@gmail.com',
    url="https://adipandas.github.io/multi-object-tracker/",
    version='0.0.1',
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'opencv-contrib-python',
        'motmetrics'
    ],
    packages=find_packages()
)

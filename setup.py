from setuptools import setup

setup(
    name='heatmap',
    license='AGPL-3.0',
    packages=['heatmap'],
    version='0.0.1',
    install_requires=[
        'pillow',
        'osmviz',
    ],
    zip_safe=False
)

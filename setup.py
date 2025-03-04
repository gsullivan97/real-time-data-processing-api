from setuptools import setup, find_packages

setup(
    name='real-time-data-processing-api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytest==7.1.2',
        'virtualenv==20.29.2',
        'fastapi==0.115.11',
        'uvicorn==0.34.0',
        'pydantic==2.10.6',
        'pandas==2.2.3',
    ],
    entry_points={
        'console_scripts': [
            'real-time-data-processing-api=src.main:main',
        ],
    },
)
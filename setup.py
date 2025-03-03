from setuptools import setup, find_packages

setup(
    name='real-time-data-processing-api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytest==7.1.2',
        'virtualenv==20.29.2'
    ],
    entry_points={
        'console_scripts': [
            'real-time-data-processing-api=real_time_data_processing_api.main:main',
        ],
    },
)
# setup.py
from setuptools import setup, find_packages

setup(
    name="ideariver_services_python",  # The name of your package
    version="0.1",
    description="A plugin-based service architecture for RabbitMQ integration.",
    author="Nima Shokouhfar",
    author_email="your.email@example.com",
    packages=find_packages(),  # Automatically find all packages
    include_package_data=True,
    install_requires=[
        "pytest",
        "pika",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum version of Python
)

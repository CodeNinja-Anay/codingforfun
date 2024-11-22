from setuptools import setup, find_packages

setup(
    name="number_circle",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "pytest>=6.0.0",  # for testing your implementation
    ],
)

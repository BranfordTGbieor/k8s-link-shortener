from setuptools import setup, find_packages

setup(
    name="url_shortener",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pytest",
        "pytest-asyncio",
    ],
) 
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="alife",
    version="0.1.0",
    author="tomato414941",
    author_email="tomato414941@gmail.com",
    description="A library for artificial life simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomato414941/alife",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    extras_require={
        "dev": ["pytest", "flake8", "black"],
        "docs": ["sphinx", "sphinx-rtd-theme"],
    },
)

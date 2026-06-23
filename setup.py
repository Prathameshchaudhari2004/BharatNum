from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="bharatnum",
    version="0.1.0",
    author="Prathamesh Chaudhari",
    author_email="prathameshchaudhari111@gmail.com",
    description="Indian Number & Currency Datatype for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Prathameshchaudhari2004/bharatnum",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.0.0",
    ],
)
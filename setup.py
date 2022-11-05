from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='payoffgraph_juttu',
    version='0.0.8',
    description='Get the most beautiful Payoff Chart using a single simple function',
    author= 'Juttu G Anurag',
    url = 'https://github.com/Juttu/ss',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['payoff graph', 'options','opstra','sensibull'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['payoffgraph_juttu'],
    package_dir={'':'src'},
    install_requires = [
        'numpy',
        'pandas',
        'streamlit',
        'plotly',
        'typing >= 3.7.4'

    ]
)
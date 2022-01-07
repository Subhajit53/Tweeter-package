import setuptools

setuptools.setup(
    name="twtr_pkg",
    version="0.1",
    author="Subhajit Ganguly",
    description="Text processing package for tweeter data",
    long_description=open('README.md').read()
    url="https://github.com/Subhajit53/Tweeter-Package",
    package_dir={"": "twtr_pkg"},
    packages=setuptools.find_packages(where="twtr_pkg"),
    python_requires=">=3.6",
)
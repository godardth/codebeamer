import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="codebeamer-client",
    version="0.0.3",
    description="Client for the CodeBeamer REST API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/godardth/codebeamer",
    author="Theophile Godard",
    author_email="theo.godard@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["codebeamer"],
    include_package_data=True,
    install_requires=[
        'requests',
    ],
)
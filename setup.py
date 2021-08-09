from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pretwita",
    version="0.1",
    author="Andrea Failla",
    author_email="andrea.failla.ak@gmail.com",
    description="A text PREprocessor for TWeets in the ITAlian language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andreafailla/pretwita",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords='nlp natural-language-processing twitter italian tweet-preprocessing',
    python_requires='>=3.0',
)
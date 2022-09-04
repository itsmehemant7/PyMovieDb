import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyMovieDb",
    version="0.0.1",
    author="Hemant Malik",
    author_email="itsmehemant7@gmail.com",
    description="A Python Module that represents IMDB API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itsmehemant7/PyMovieDb",
    packages=setuptools.find_packages(),
    zip_safe=False
)
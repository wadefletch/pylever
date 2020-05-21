import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylever",  # Replace with your own username
    version="0.1.0",
    author="Wade Fletcher",
    author_email="wbfletch@iu.edu",
    description="Python bindings for the Lever.co Postings API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wadefletch/pylever",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

import setuptools

# Developer self-reminder for uploading in pypi:
# - install: wheel, twine
# - build  : python setup.py bdist_wheel
# - deploy : twine upload dist/*

# with open("README.md", "r") as file:
#    long_description = file.read()

long_description = (
    "A package for discovering biases and suggesting mitigation approaches <br>"
)

setuptools.setup(
    name="cvbiasmitigation",
    version="0.0.1",
    author="Ioannis Sarridis",
    author_email="gsarridis@iti.gr",
    description="A package for discovering biases and suggesting mitigation approaches",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gsarridis/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "scipy",
        "pandas",
    ],
    python_requires=">=3.6",
    package_data={"cvbiasmitigation": ["./data/rfw.csv"]},
    include_package_data=True,
)

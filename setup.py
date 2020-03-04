import setuptools

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="getostheme",
	version="2020.1",
	author="FredHappyface",
	description="Use this module to get the OS theme (dark/light)",
	long_description=long_description,
    long_description_content_type="text/markdown",
	url="https://github.com/FredHappyface/Python.GetOSTheme",
	packages=setuptools.find_packages(),
	classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
	python_requires='>=3.0',
)

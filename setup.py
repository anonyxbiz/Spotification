from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="Spotification",
    version="1.0.1",
    description="Spotification is a fast and efficient reverse-engineered Spotify API, allowing unlimited access to Spotify's private API without the need for API keys. It provides access to all Spotify API routes, including private routes and data.",
    author="Anonyxbiz",
    author_email="biz@anonyxis.life",
    url="https://github.com/anonyxbiz/Spotification",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['Spotification'],
    python_requires='>=3.6',
)

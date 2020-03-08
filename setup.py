from setuptools import find_packages, setup


# Package meta-data.
NAME = 'amethyst-crayon-railroads'
DESCRIPTION = "A game engine for playing railroad-building games."
URL = 'https://github.com/jbradberry/amethyst-crayon-railroads'
EMAIL = 'jeff.bradberry@gmail.com'
AUTHOR = 'Jeff Bradberry'
# REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

REQUIRED = [
    'amethyst-games',
]


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description="",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Games/Entertainment',
    ],
)

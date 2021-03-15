import setuptools

__version__ = '0.1.6'

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='PyDoge',
    version=__version__,
    author='Ezequiel Portela',
    author_email='eportelab@gmail.com',
    description='A common functions and helpers library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ezeportela/pydoge',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=install_requires,
    python_requires='>=3.6'
)

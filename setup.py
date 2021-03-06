from setuptools import find_packages, setup

with open('commando/_meta.py') as version_file:
    exec(version_file.read())

with open('README.md') as r:
    readme = r.read()

setup(
    name='ComManDo',
    description=readme,
    version=__version__,
    packages=find_packages(exclude=('tests')),
    install_requires=[
        'anndata',
        'matplotlib',
        'numpy',
        'scikit-learn-extra',
        'scanpy',
        'scipy',
        'sklearn',
        'torch',
        'torchvision',
        'umap',
        'unioncom',
    ],
    extras_require={
        'dev': [
            'flake8',
            'flake8-docstrings',
            'flake8-import-order',
            'openpyxl',
            'pip-tools',
            'pytest',
            'pytest-cov',
        ],
        'notebooks': [
            'jupyterlab',
            'mmd_wrapper @ git+https://git@github.com/Oafish1/WR2MD',
            'pandas',
            'seaborn',
        ],
    },
	tests_require=['pytest'],
)

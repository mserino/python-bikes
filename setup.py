try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Boris Bikes',
    'author': 'Margherita Serino',
    'url': 'http://github.com/python-bikes',
    'download_url': 'http://github.com/python-bikes',
    'author_email': 'serino.marghe@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'python-bikes'
}

setup(**config)
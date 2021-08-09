import os
from .pretwita import PreTwITA

__version__ = '0.1'
__license__ = 'GPLv3'
__author__ = 'Andrea Failla'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

__all__ = [
    'PreTwITA'
]
try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

from .mom6_regional import *  # noqa

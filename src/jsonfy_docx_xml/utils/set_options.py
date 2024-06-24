"""
Utilities for setting options that change how the document is traversed
"""


from typing import Dict, Union, Type
from ..iterators.generic import register_iterator, build_iterators


def set_options(options: Dict[str, Union[str, bool, int, float]]) -> None:
    """
    Register iterators depending on the selected options
    """

    build_iterators()






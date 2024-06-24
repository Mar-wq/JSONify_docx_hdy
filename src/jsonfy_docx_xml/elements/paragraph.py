"""
Elements which inherit from EG_PContent
"""
from typing import Optional, Dict, List, Any, Sequence, Iterator

from more_itertools import peekable

from . import el, container



class paragraph(container):
    """ 
    Represents a simple paragraph
    """

    __type__ = "CT_P"
    __props__ = ['alignment', 'text']















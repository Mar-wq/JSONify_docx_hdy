from . import el, container
from ..types import xmlFragment


class text(el):
    """
    A Text element
    """

    __type__ = "CT_Text"
    __props__ = ["text"]

"""
The body element
"""
from typing import Dict, Any, Optional, Iterator
from more_itertools import peekable
from .base import container


class body(container):
    """
    A document body element
    """

    __type__ = "CT_Body"

    def to_json(
        self, doc, options: Dict[str, str] = None, super_iter: Optional[Iterator] = None
    ) -> Dict[str, Any]:
        """
        Coerce a container object to JSON
        """
        contents = []
        iter_me = peekable(self)   #可用于在不消耗迭代器的情况下查看当前迭代对象
        for elt in iter_me:
            JSON = elt.to_json(doc, options, iter_me)

            contents.append(JSON)

        out: Dict[str, Any] = {"TYPE": self.__type__, "VALUE": contents}
        return out

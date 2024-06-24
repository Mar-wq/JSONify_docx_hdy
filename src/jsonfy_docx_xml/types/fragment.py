"""
Abstract classes for typing purposes only
"""
# pylint: disable=no-self-use,pointless-statement,missing-docstring,invalid-name, too-few-public-methods
from __future__ import annotations
from typing import Optional, Dict, Sequence

class xmlFragment:
    """an abstract class representing the xml fragments returned by python-docx
    """
    def getchildren(self) -> Sequence[xmlFragment]:
        ...
    def getparent(self) -> Optional[xmlFragment]:
        ...
    def getnext(self) -> Optional[xmlFragment]:
        ...
    def xpath(self, x:str) -> Optional[xmlFragment]: # XPath（XML Path Language） pylint: disable=unused-argument 根据 XPath 表达式查找元素。返回类型是 Optional[xmlFragment]，表示返回值可以是 xmlFragment 类型或 None。
        ...


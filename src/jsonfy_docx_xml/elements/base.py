from typing import Optional, Dict, Any, Sequence, Generator, Iterator

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.shared import CT_String, CT_OnOff, CT_DecimalNumber
from docx.shared import  Twips
from more_itertools import peekable

from ..types import xmlFragment



class el:
    """
    Abstract base class for docx element
    """
    __type__: str
    parent: "el"
    fragment: xmlFragment                 #表示由python-docx解析出的Document中的element类对象及其子类对象
    __iter_name__: Optional[str] = None
    __iter_xpath__: Optional[str] = None
    props: Dict[str, Any]

    def __init__(self, x: xmlFragment):
        self.fragment = x

    def to_json(self, doc) -> Dict[str, Any]:# pylint: disable=unused-argument
        """
        coerce an object to JSON
        """

        out = {"type": self.__type__}

        if hasattr(self, 'props'):
            for key, prop in self.props.items():
                out[key] = prop
        return out





def get_val(x):
    """
    Extract the value from a simple property
    """
    if isinstance(x, (str,bool)):
        return x
    if isinstance(x, list):
        return [get_val(elt) for elt in x]
    if isinstance(x, (CT_String, CT_OnOff, CT_DecimalNumber)):
        return x.val
    if isinstance(x, (Twips)):
        return x.twips
    if isinstance(x, WD_PARAGRAPH_ALIGNMENT):  # 添加对齐方式的处理
        return x.name  # 或者使用 x.value 根据需求提取
    raise RuntimeError("Unexpected value type '%s'" % x.__class__.__name__)


class container(el):
    """
    Represents an object that can contain other objects
    """



    def __iter__(self) -> Generator['el', None, None]:
        from ..iterators import xml_iter
        node: xmlFragment = (self.fragment
                             if self.__iter_xpath__ is None
                             else self.fragment.xpath(self.__iter_xpath__))
        for elt in xml_iter(node,
                            self.__iter_name__ if self.__iter_name__ else self.__type__):
            yield elt


    def to_json(self, doc) -> Dict[str, Any]:
        """Coerce a container object to JSON
        """

        out = super().to_json(doc)
        contents = []
        iter_me = peekable(self)   #可用于在不消耗迭代器的情况下查看当前迭代对象
        for elt in iter_me:
            JSON = elt.to_json(doc)

            contents.append(JSON)

        # out: Dict[str, Any] = {"TYPE": self.__type__, "VALUE": contents}
        if contents:
            out.update({"VALUE": contents})

        return out
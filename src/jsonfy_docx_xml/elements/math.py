from typing import Dict, Any

from docx.oxml.ns import qn
from lxml import etree

from jsonfy_docx_xml.elements import el


class math(el):
    __type__ = "formulas"

    def __init__(self, x):
        # 将element对象转换为字符串
        self.omml_str = etree.tostring(x, encoding='unicode')
        print()

    def to_json(self, doc) -> Dict[str, Any]:
        out =  super().to_json(doc)

        out.update({'omml_str': self.omml_str})
        return out


class mathParagraph(math):
    __type__ = "formulas"

    def __init__(self, x):
        omath_element = x.find(qn('m:oMath'))
        self.omml_str= etree.tostring(omath_element, pretty_print=True, encoding='unicode')
        print()

import base64
from typing import Dict, Any

from PIL import Image
from docx.oxml.ns import qn
from lxml import etree
from io import BytesIO

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


class embObject(el):
    __type__ = "embObject"
    def __init__(self, x):
        imagedata_element = x.xpath('.//v:imagedata', namespaces=x.nsmap)
        imagedata_element = imagedata_element[0]
        rId = imagedata_element.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        self.rId = rId


    def to_json(self, doc) -> Dict[str, Any]:
        out =  super().to_json(doc)
        if self.rId:
            rel = doc.part.rels[self.rId]
            image_part = rel.target_part
            data = image_part.blob
            ext = rel.target_ref.split('.')[-1]  # 获取扩展名
            # 通过rId直接获取对应的图像数据
            # image_part = doc.part.rels.get(self.rId).target_part
            # image_data = image_part.blob

            # 使用PIL显示图片
            base64_data = base64.b64encode(data).decode('utf-8')

            temp = {"blob": base64_data, "ext": ext}
            out.update(temp)
            return out

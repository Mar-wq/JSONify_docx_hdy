import base64
from typing import Dict, Any

from docx import Document, ImagePart

from jsonfy_docx_xml.elements import el

from docx.document import Document
from docx.text.paragraph import Paragraph
from docx.image.image import Image
from docx.parts.image import ImagePart




class image(el):
    """
    A Text element
    """

    __type__ = "CT_Drawing"
    __props__ = ["text"]


    def __init__(self, x):
        super().__init__(x)
        # 获取软连接的信息
        img = x.xpath('.//pic:pic')[0]
        self.embed = img.xpath('.//a:blip/@r:embed')[0]

    def to_json(self, doc) -> Dict[str, Any]:
        out =  super().to_json(doc)

        #通过软连接直接拿到图片数据
        related_part: ImagePart = doc.part.related_parts[self.embed]
        image: Image = related_part.image
        # 后缀
        ext = image.ext

        # 二进制内容
        blob = image.blob
        base64_data = base64.b64encode(blob).decode('utf-8')
        temp = {"blob": base64_data, "ext": ext}
        out.update(temp)
        return out

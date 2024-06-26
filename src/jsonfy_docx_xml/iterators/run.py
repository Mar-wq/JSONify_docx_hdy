from docx.oxml.ns import qn

from jsonfy_docx_xml.elements.image import image
from jsonfy_docx_xml.elements.math import math, embObject
from jsonfy_docx_xml.iterators.generic import register_iterator

register_iterator("run",
                  TAGS_TO_YIELD={qn("w:drawing"):image,
                                 qn("m:oMath"):math,
                                 qn("w:object"):embObject})
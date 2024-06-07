from docx.oxml.ns import qn
from ..elements import body
from .generic import register_iterator
from ..elements.base import container

register_iterator(
    "CT_Document",
    TAGS_TO_YIELD={qn("w:body"): body},
)

from docx.oxml.ns import qn

from jsonfy_docx_xml.elements.paragraph import paragraph
from jsonfy_docx_xml.elements.table import tr, tc, table
from jsonfy_docx_xml.elements.text import text
from jsonfy_docx_xml.iterators.generic import register_iterator


register_iterator("CT_Tbl", TAGS_TO_YIELD={qn("w:tr"):tr})
register_iterator("CT_Tr", TAGS_TO_YIELD={qn("w:tc"):tc})
register_iterator("CT_Tc", TAGS_TO_YIELD={qn("w:p"): paragraph, qn("w:tbl"): table})
from jsonfy_docx_xml.elements.math import math, mathParagraph
from jsonfy_docx_xml.elements.paragraph import commentRangeStart, commentRangeEnd
from jsonfy_docx_xml.elements.run import run
from jsonfy_docx_xml.iterators.generic import register_iterator
from docx.oxml.ns import qn

register_iterator("paragraph", TAGS_TO_YIELD={
    qn("w:r"):run,
    qn("m:oMath"):math,
    qn("m:oMathPara"):mathParagraph,
    qn("w:commentRangeStart"): commentRangeStart,
    qn("w:commentRangeEnd"):commentRangeEnd
})
#register_iterator("CT_P", TAGS_TO_YIELD = { qn("w:t"): text}, extends=["EG_PContent"])